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
    error_message = "Minimalny rok produkcji jest większy od maksymalnego"

    year_output = input_hint(year_output, year_style_dict, year_input_1,
                             year_input_2, 2000, 2019, error_message, "")

    # 3. Mileage
    mileage_output = "Przebieg: "
    mileage_style_dict = {"width": "15%", "position": "absolute",
                          "left": "35%",
                          "top": "10%", "height": "10%", "font-size": 18,
                          "font-family": "Cambria"}
    error_message = "Minimalny przebieg jest większy od maksymalnego"

    mileage_output = input_hint(mileage_output, mileage_style_dict,
                                mileage_input_1, mileage_input_2, 1e4, 1e6,
                                error_message, "km")

    return [price_output, price_style_dict, year_output, year_style_dict,
            mileage_output, mileage_style_dict]
