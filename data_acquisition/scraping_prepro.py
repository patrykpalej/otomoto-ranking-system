def scraping_prepro(filters_json):
    url = "https://www.otomoto.pl/osobowe/"

    filters = {
        "search[category_id]": "29",
        
        "search[filter_enum_make]": filters_json["brand"],
        "search[filter_enum_model]": filters_json["model"],
        
        "search[filter_float_price:from]": filters_json["min_price"],
        "search[filter_float_price:to]": filters_json["max_price"],
        
        "search[filter_float_year:from]": filters_json["min_year"],
        "search[filter_float_year:to]": filters_json["max_year"],

        "search[filter_float_mileage:from]": filters_json["min_mileage"],
        "search[filter_float_mileage:to]": filters_json["max_mileage"],

        "search[filter_enum_fuel_type]": filters_json["fuel_type"],

        "search[filter_enum_has_vin]": filters_json["has_vin"],

        "search[filter_enum_damaged]": filters_json["damaged"],
        "search[filter_enum_no_accident]": filters_json["no_accident"]
        }

    return url, filters, filters_json["max_distance"]
