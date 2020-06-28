import os
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from data_acquisition.db_funcs import create_table, read_from_table
from output_presentation.transform_raw_offers import transform_raw_offers
from output_presentation.select_rows import select_rows
from output_presentation.sort_by_rating import sort_by_rating


# 1. Read raw offers
Base = declarative_base()
Offers, engine = create_table(Base)
Session = sessionmaker(bind=engine)
session = Session()

raw_offers = read_from_table(session, Offers)


# 2. Transform raw offers into a df
df = transform_raw_offers(raw_offers)


# 3. Get chosen rows based on conditions (e.g. offer_timestamp)
df_filtered = select_rows(df)


# 4. Sort by overall rating
df_sorted = sort_by_rating(df_filtered)


# 5. Write n best offers to file
n = 10
day = str(datetime.now().day)
month = str(datetime.now().month)

date = month + '.' + day
if not os.path.isdir(os.getcwd() + "/results/" + date):
    os.mkdir(os.getcwd() + "/results/" + date)

df_best = df_sorted.iloc[:5]
df_best.index = range(1, len(df_best)+1)
df_best.to_csv('results/{}/{}.csv'.format(date, date), sep=';')
