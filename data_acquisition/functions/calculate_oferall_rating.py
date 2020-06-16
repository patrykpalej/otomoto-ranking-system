def calculate_oferall_rating(offer):

    offer["overall"] = offer["mileage"] * offer["price"] / 1e8

    return offer
