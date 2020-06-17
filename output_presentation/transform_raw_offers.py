import pandas as pd


def transform_raw_offers(raw_offers):

    df = pd.DataFrame(columns=["price", "prod_year", "brand", "model",
                               "distance", "overall", "scraping_timestamp",
                               "link"])
    # change types
    df["price"] = df["price"].astype("int64")
    df["distance"] = df["distance"].astype("float")

    for offer in raw_offers:
        parameters = list()

        parameters.append(offer.price)
        parameters.append(offer.prod_year)
        parameters.append(offer.brand)
        parameters.append(offer.model)
        parameters.append(float(offer.distance))
        parameters.append(float(offer.overall))
        parameters.append(offer.scraping_timestamp)
        parameters.append(offer.link)

        df.loc[len(df)] = parameters

    return df
