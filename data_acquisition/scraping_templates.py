import io
import json

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data_acquisition.functions.db_funcs import create_table, delete_table

from data_acquisition.functions.scraping_prepro import scraping_prepro
from data_acquisition.functions.initial_search import initial_search
from data_acquisition.functions.scrape_single_offer import scrape_single_offer
from data_acquisition.functions.get_all_urls import get_all_urls
from data_acquisition.functions.write_in_db import write_in_db


max_distance = 200
# 1. Initial actions
url, filters = scraping_prepro()
initial_soup, initial_url = initial_search(url, filters, max_distance)
offers_urls = get_all_urls(initial_soup)

# 2. Actual scraping
offers = []
for single_offer_url in offers_urls:
    offers.append(scrape_single_offer(single_offer_url))

# offer_specification =

# 3. Save the results to db
Base = declarative_base()
Offers, engine = create_table(Base)

Session = sessionmaker(bind=engine)

session = Session()
delete_table(session, Offers, engine)
session = Session()
write_in_db(session, Offers, offers)

# 4. Save to json
# with open("offers.json", "w", encoding="utf-8") as write_file:
#     json.dump(offers, write_file)

# with io.open("output.html", "w", encoding="utf-8") as f:
#     f.write(str(initial_soup))
