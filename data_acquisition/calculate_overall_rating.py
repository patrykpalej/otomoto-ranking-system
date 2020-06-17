def calculate_overall_rating(offer):

    offer["overall"] = offer["mileage"] * offer["price"] / 1e8

    return offer
