from sqlalchemy import create_engine, Column, Integer, String, Boolean, \
    DateTime


def create_table(base):
    class Offers(base):
        __tablename__ = "Offers"
        offer_id = Column("id", Integer, unique=True, primary_key=True)
        price = Column("Price", Integer)
        prod_year = Column("Year", Integer)
        mileage = Column("Mileage", Integer)
        fuel = Column("Fuel", String)
        color = Column("Color", String)
        brand = Column("Brand", String)
        crashed = Column("Crashed", Boolean)
        offer_timestamp = Column("Offer timestamp", DateTime)
        scraping_timestamp = Column("Scraping timestamp", DateTime)
        overall = Column("Overall rating")

    engine = create_engine("postgresql+psycopg2://postgres:postgres"
                           "@localhost/postgres")
    base.metadata.create_all(bind=engine)

    return Offers, engine


def delete_table(session, table, engine):
    table.__table__.drop(engine)

    session.close()


def update_table(session, offer_class, values):
    offer = offer_class()

    offer.offer_id = values["id"]
    offer.price = values["price"]
    offer.prod_year = values["prod_year"]
    offer.mileage = values["mileage"]
    offer.fuel = values["fuel"]
    offer.color = values["color"]
    offer.brand = values["brand"]
    offer.crashed = values["crashed"]
    offer.offer_timestamp = values["offer_timestamp"]
    offer.scraping_timestamp = values["scraping_timestamp"]
    offer.overall = values["overall"]

    session.add(offer)
    session.commit()
    session.close()


def read_from_table(session, offer_class, where_column, where_value):
    output = session.query(offer_class).all()  #filter_by().all()
    session.close()

    return output
