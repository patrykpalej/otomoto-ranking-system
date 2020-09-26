from datetime import datetime


def calculate_overall_rating(offer):

    # Power, mileage, price
    overall = 1e10 * offer["power"] / (offer["mileage"] * offer["price"])

    # Owner
    if offer["owner"] == "Firma":
        overall = overall * 0.8

    # Fuel
    if offer["fuel"] == "Benzyna+LPG":
        overall = overall*1.1

    # Year
    age = datetime.now().year - offer["prod_year"]
    overall = overall * (1 - 0.074*age + 0.0024*age**2)

    # Distance
    overall = overall * (1 - 0.003*offer["distance"])

    return round(overall, 2)
