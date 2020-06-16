from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data_acquisition.functions.db_funcs import create_table, delete_table


Base = declarative_base()
Offers, engine = create_table(Base)
Session = sessionmaker(bind=engine)

# -------
session = Session()
delete_table(session, Offers, engine)
# -------
