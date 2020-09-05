from funcs import *


def backend(price_input_1, price_input_2, year_input_1, year_input_2,
            mileage_input_1, mileage_input_2):
    # 1. Price
    min_price = 2000
    max_price = 80000
    price_output = "Cena: "
    price_style_dict = {"width": "15%", "position": "absolute", "left": "5%",
                        "top": "10%", "height": "10%", "font-size": 18,
                        "font-family": "Cambria"}
    error_message = "Minimalna cena jest większa od maksymalnej"

    price_output, price_min_limit, price_max_limit \
        = input_hint(price_output, price_style_dict, price_input_1,
                     price_input_2, min_price, max_price, error_message, "zł",
                     1)

    # 2. Production year
    min_year = 2000
    max_year = 2019
    year_output = "Rok produkcji: "
    year_style_dict = {"width": "15%", "position": "absolute", "left": "20%",
                       "top": "10%", "height": "10%", "font-size": 18,
                       "font-family": "Cambria"}
    error_message = "Minimalny rok produkcji jest większy od maksymalnego"

    year_output, year_min_limit, year_max_limit \
        = input_hint(year_output, year_style_dict, year_input_1,
                     year_input_2, min_year, max_year, error_message, "", 0)

    # 3. Mileage
    min_mil = int(1e4)
    max_mil = int(1e6)
    mileage_output = "Przebieg: "
    mileage_style_dict = {"width": "15%", "position": "absolute",
                          "left": "35%", "top": "10%", "height": "10%",
                          "font-size": 18, "font-family": "Cambria"}
    error_message = "Minimalny przebieg jest większy od maksymalnego"

    mileage_output, mileage_min_limit, mileage_max_limit \
        = input_hint(mileage_output, mileage_style_dict, mileage_input_1,
                     mileage_input_2, min_mil, max_mil, error_message, "km",
                     1)

    return [price_output, price_style_dict, year_output, year_style_dict,
            mileage_output, mileage_style_dict]
