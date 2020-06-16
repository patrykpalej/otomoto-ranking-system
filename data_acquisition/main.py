import json
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data_acquisition.functions.db_funcs import create_table, delete_table

from data_acquisition.functions.scraping_prepro import scraping_prepro
from data_acquisition.functions.initial_search import initial_search
from data_acquisition.functions.scrape_single_offer import scrape_single_offer
from data_acquisition.functions.calculate_overall_rating import \
    calculate_overall_rating
from data_acquisition.functions.get_all_urls import get_all_urls
from data_acquisition.functions.write_to_db import write_to_db


# I. Create table
Base = declarative_base()
Offers, engine = create_table(Base)
Session = sessionmaker(bind=engine)

# -------
# session = Session()
# delete_table(session, Offers, engine)
# -------


# II. Get and save data
filters_json = json.load(open("filters.json", "r"))

for filters_set in filters_json:
    # 1. Initial actions
    url, filters, max_dist = scraping_prepro(filters_set)
    initial_soup, initial_url = initial_search(url, filters, max_dist)
    offers_urls = get_all_urls(initial_soup)
    # print(initial_url)

    # 2. Actual scraping
    offers = []
    for single_offer_url in offers_urls:
        offer = scrape_single_offer(single_offer_url)
        offer = calculate_overall_rating(offer)
        offers.append(offer)

    # 3. Write scraped offers to database
    write_to_db(Session, Offers, offers)
