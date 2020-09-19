import time
import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from data_acquisition.db_funcs import create_tables, delete_table, \
    read_from_table, delete_old_offers
from data_acquisition.scraping_prepro import scraping_prepro
from data_acquisition.initial_search import initial_search
from data_acquisition.scrape_single_offer import scrape_single_offer
from data_acquisition.calculate_overall_rating import calculate_overall_rating
from data_acquisition.get_all_urls import get_all_urls
from data_acquisition.write_to_db import write_to_db


# I. Create table and get IDs already in database
Base = declarative_base()
Offers, MyOffers, engine = create_tables(Base)
Session = sessionmaker(bind=engine)

session = Session()
db_offers = read_from_table(session, Offers)
offers_ids = [off.offer_id for off in db_offers]

session = Session()
db_myoffers = read_from_table(session, MyOffers)
myoffers_ids = [off.offer_id for off in db_myoffers]


# II. Delete offers older than X
max_offer_days = 14
session = Session()
delete_old_offers(session, MyOffers, engine)

# -------
# session = Session()
# delete_table(session, Offers, engine)
# delete_table(session, MyOffers, engine)
# -------

# III. Get and save data
filters_json = json.load(open("data_acquisition/filters.json", "r"))  # cmd
# filters_json = json.load(open("filters.json", "r"))  # pycharm
for i, filters_set in enumerate(filters_json):
    # 1. Initial actions
    url, filters, max_dist = scraping_prepro(filters_set)
    initial_soup, initial_url = initial_search(url, filters, max_dist)
    scraped_ids = myoffers_ids if filters_set["my_offers"] else offers_ids
    offers_urls = get_all_urls(initial_soup, scraped_ids)

    # 2. Actual scraping
    offers_list = []
    invalid_offers = 0
    for single_offer_url in offers_urls:
        time.sleep(0.5)
        offer = scrape_single_offer(single_offer_url)
        if offer == 0:
            invalid_offers += 1
            continue

        if filters_set["my_offers"]:
            offer["overall"] = calculate_overall_rating(offer)

        if offer["distance"] <= filters_set["max_distance"] \
                or not filters_set["my_offers"]:
            offers_list.append(offer)

    # 3. Write scraped offers to database
    if filters_set["my_offers"]:
        write_to_db(Session, MyOffers, offers_list, 1)
    else:
        write_to_db(Session, Offers, offers_list, 0)
