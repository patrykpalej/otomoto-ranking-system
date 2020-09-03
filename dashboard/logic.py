from funcs import *


def backend(price_input_1, price_input_2, year_input_1, year_input_2,
            mileage_input_1, mileage_input_2):
    # 1. Price
    min_limit = 2000
    max_limit = 80000
    price_output = "Cena: "
    price_style_dict = {"width": "15%", "position": "absolute", "left": "5%",
                        "top": "10%", "height": "10%", "font-size": 18,
                        "font-family": "Cambria"}

    if price_input_1:
        min_limit = int(price_input_1)

    if price_input_2:
        max_limit = int(price_input_2)

    price_output \
        += str('{:,}'.format(min_limit).replace(",",  " ")) \
        + "zł - " + str('{:,}'.format(max_limit).replace(",", " ")) \
          + "zł"

    if price_input_1 or price_input_2:
        try:
            if int(price_input_1) < 2000 or int(price_input_2) > 80000:
                price_output = "Wybierz z zakresu 2 000zł - 80 000zł"
                price_style_dict["color"] = "red"
        except TypeError:
            pass

        try:
            if int(price_input_1) > int(price_input_2):
                price_output = "Cena minimalna jest większa od maksymalnej"
                price_style_dict["color"] = "red"
        except TypeError:
            pass

    # 2. Production year
    year_output = "Rok produkcji: "
    year_style_dict = {"width": "15%", "position": "absolute", "left": "20%",
                       "top": "10%", "height": "10%", "font-size": 18,
                       "font-family": "Cambria"}

    if year_input_1 and year_input_2:
        year_output += year_input_1 + " - " + year_input_2

        if int(year_input_1) < 2000 or int(year_input_2) > 2019:
            year_output = "Wybierz z zakresu 2000 - 2019"
            year_style_dict["color"] = "red"

        if int(year_input_1) > int(year_input_2):
            year_output = "Minimalny rok produkcji jest większy od " \
                          "maksymalnego"
            year_style_dict["color"] = "red"

    # 3. Mileage
    mileage_output = "Przebieg: "
    mileage_style_dict = {"width": "15%", "position": "absolute",
                          "left": "35%",
                          "top": "10%", "height": "10%", "font-size": 18,
                          "font-family": "Cambria"}

    if mileage_input_1 and mileage_input_2:
        mileage_output += mileage_input_1 + "km - " + mileage_input_2 + "km"

        if int(mileage_input_1) < 1e4 or int(mileage_input_2) > 1e6:
            mileage_output = "Wybierz z zakresu 10k - 1M"
            mileage_style_dict["color"] = "red"

        if int(mileage_input_1) > int(mileage_input_2):
            mileage_output = "Minimalny przebieg jest większy od maksymalnego"
            mileage_style_dict["color"] = "red"

    return [price_output, price_style_dict, year_output, year_style_dict,
            mileage_output, mileage_style_dict]
