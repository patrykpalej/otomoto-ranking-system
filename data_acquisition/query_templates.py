from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from data_acquisition.db_funcs import create_table, delete_table, \
    update_table, read_from_table


# 1. Create table if doesn't exist
Base = declarative_base()
Offers, engine = create_table(Base)


# 2. Inserting data
Session = sessionmaker(bind=engine)
session = Session()

values = {"id": 12223, "price": 10000, "prod_year": 2004, "mileage": 30000,
          "fuel": "benzyna", "color": "czarny", "brand": "Ford",
          "crashed": bool(1),
          "offer_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          "scraping_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          "overall": 0}
try:
    update_table(session, Offers, values)
except:
    print("Offer already in database")
    session.close()


# 3. Read from database
session = Session()
db_output = read_from_table(session, Offers, "age", 3)


# 4. Delete table
# delete_table(session, Offers, engine)

