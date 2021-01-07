from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
    Numeric


def create_tables(base):
    # Offers
    class Offers(base):
        __tablename__ = "Offers"
        # row_id = Column(Integer, primary_key=True, autoincrement=True)
        offer_id = Column("id", String, unique=False, primary_key=True)
        price = Column("Price", Integer)
        owner = Column("Owner", String)
        prod_year = Column("Year", Integer)
        mileage = Column("Mileage", Integer)
        fuel = Column("Fuel", String)
        color = Column("Color", String)
        brand = Column("Brand", String)
        model = Column("Model", String)
        power = Column("Power", Integer)
        link = Column("Link", String)
        longitude = Column("Longitude", Numeric)
        latitude = Column("Latitude", Numeric)
        # distance = Column("Distance", Numeric)
        location = Column("Location", String)
        offer_timestamp = Column("Offer timestamp", DateTime)
        scraping_timestamp = Column("Scraping timestamp", DateTime)

    # MyOffers
    class MyOffers(base):
        __tablename__ = "MyOffers"
        offer_id = Column("id", String, unique=False, primary_key=True)
        price = Column("Price", String)
        owner = Column("Owner", String)
        prod_year = Column("Year", Integer)
        mileage = Column("Mileage", Integer)
        fuel = Column("Fuel", String)
        brand = Column("Brand", String)
        model = Column("Model", String)
        power = Column("Power", Integer)
        link = Column("Link", String)
        longitude = Column("Longitude", Numeric)
        latitude = Column("Latitude", Numeric)
        distance = Column("Distance", Numeric)
        offer_timestamp = Column("Offer timestamp", DateTime)
        scraping_timestamp = Column("Scraping timestamp", DateTime)
        overall = Column("Overall rating", Numeric)

    engine = create_engine("postgresql+psycopg2://postgres:postgres"
                           "@mydbs.cjkpvohborum.eu-central-1.rds.amazonaws.com/otomoto")
    base.metadata.create_all(bind=engine)

    return Offers, MyOffers, engine


def delete_table(session, table, engine):
    session.query(table).delete()
    session.commit()
    session.close()


def delete_old_offers(session, table, max_offer_days):
    session.query(table).filter(table.offer_timestamp < datetime.now()
                                - timedelta(days=14)).delete()

    session.commit()
    session.close()


def update_table(session, offers_class, values, is_myoffers):

    if not is_myoffers:
        # Offers
        offer = offers_class()

        offer.offer_id = values["id"]
        offer.price = values["price"]
        offer.owner = values["owner"]
        offer.prod_year = values["prod_year"]
        offer.mileage = values["mileage"]
        offer.fuel = values["fuel"]
        offer.color = values["color"]
        offer.brand = values["brand"]
        offer.model = values["model"]
        offer.power = values["power"]
        offer.link = values["link"]
        offer.longitude = values["longitude"]
        offer.latitude = values["latitude"]
        # offer.distance = values["distance"]
        offer.location = values["location"]
        offer.offer_timestamp = values["offer_timestamp"]
        offer.scraping_timestamp = values["scraping_timestamp"]

        session.add(offer)
        session.commit()
        session.close()
    else:
        # MyOffers
        myoffer = offers_class()

        myoffer.offer_id = values["id"]
        myoffer.price = values["price"]
        myoffer.owner = values["owner"]
        myoffer.prod_year = values["prod_year"]
        myoffer.mileage = values["mileage"]
        myoffer.fuel = values["fuel"]
        myoffer.brand = values["brand"]
        myoffer.model = values["model"]
        myoffer.power = values["power"]
        myoffer.link = values["link"]
        myoffer.longitude = values["longitude"]
        myoffer.latitude = values["latitude"]
        myoffer.distance = values["distance"]
        myoffer.offer_timestamp = values["offer_timestamp"]
        myoffer.scraping_timestamp = values["scraping_timestamp"]
        myoffer.overall = values["overall"]

        session.add(myoffer)
        session.commit()
        session.close()


def read_from_table(session, offer_class):
    output = session.query(offer_class).all()  #filter_by().all()
    session.close()

    return output
