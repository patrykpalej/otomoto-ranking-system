def scraping_prepro():
    url = "https://www.otomoto.pl/osobowe/"

    filters = {
        "search[category_id]": "29",
        
        # "search[filter_enum_make]": "toyota",
        # "search[filter_enum_model]": "yaris",
        
        "search[filter_float_price:from]": "20000",
        "search[filter_float_price:to]": "30000",
        
        "search[filter_float_year:from]": "2014",
        "search[filter_float_year:to]": "2015",
        
        "search[filter_float_mileage:from]": "10000",
        "search[filter_float_mileage:to]": "90000",
        
        "search[filter_enum_fuel_type]": "petrol-lpg",

        "search[filter_enum_has_vin]": "1"
        }
    
    return url, filters
