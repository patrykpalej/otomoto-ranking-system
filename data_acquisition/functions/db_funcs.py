from sqlalchemy import create_engine, Column, Integer, String, DateTime


def create_table(base):
    class Offers(base):
        __tablename__ = "Offers"
        offer_id = Column("id", String, unique=True, primary_key=True)
        price = Column("Price", Integer)
        prod_year = Column("Year", String)
        mileage = Column("Mileage", Integer)
        fuel = Column("Fuel", String)
        color = Column("Color", String)
        brand = Column("Brand", String)
        model = Column("Model", String)
        link = Column("Link", String)
        offer_timestamp = Column("Offer timestamp", DateTime)
        scraping_timestamp = Column("Scraping timestamp", DateTime)
        overall = Column("Overall rating", Integer)

    engine = create_engine("postgresql+psycopg2://postgres:postgres"
                           "@localhost/postgres")
    base.metadata.create_all(bind=engine)

    return Offers, engine


def delete_table(session, table, engine):
    session.query(table).delete()
    session.commit()

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
    offer.model = values["model"]
    offer.link = values["link"]
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
