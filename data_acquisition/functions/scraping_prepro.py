def scraping_prepro():
    url = "https://www.otomoto.pl/osobowe/"

    filters = {
        "search[category_id]": "29",
        
        # "search[filter_enum_make]": "toyota",
        # "search[filter_enum_model]": "yaris",
        
        "search[filter_float_price:from]": "20000",
        "search[filter_float_price:to]": "40000",
        
        "search[filter_float_year:from]": "2010",
        "search[filter_float_year:to]": "2015",
        
        "search[filter_float_mileage:from]": "60000",
        "search[filter_float_mileage:to]": "90000",
        
        "search[filter_enum_fuel_type]": "petrol",

        "search[filter_enum_has_vin]": "1",

        "search[filter_enum_damaged]": "0",
        "search[filter_enum_no_accident]": "1"
        }

    return url, filters
