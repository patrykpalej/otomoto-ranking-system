import pandas as pd
from db_funcs import create_tables
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from funcs_filters import *
from funcs_plotsettings import *
from funcs_plots import *


def backend(price_input_1, price_input_2, year_input_1, year_input_2,
            mileage_input_1, mileage_input_2, power_input_1, power_input_2,
            fuel_input, brand_input, in_0_0, in_0_1, in_0_2, in_0_3, in_1_0,
            in_1_1, in_1_2, in_1_3, link_search_in):

    Base = declarative_base()
    Offers, MyOffers, engine = create_tables(Base)
    Session = sessionmaker(bind=engine)
    session = Session()
    output = session.query(MyOffers).all()
    session.close()
    # brands_list = [off.brand for off in output]
    df = pd.DataFrame({"Price": [int(off.price) for off in output],
                       "Year": [off.prod_year for off in output],
                       "Mileage": [off.mileage for off in output],
                       "Power": [int(off.power) for off in output],
                       "Fuel": [off.fuel for off in output],
                       "Brand": [off.brand for off in output],
                       "Longitude": [off.longitude for off in output],
                       "Latitude": [off.latitude for off in output],
                       "Link": [off.link for off in output]})
    df = df[df["Power"] > 0]

    # df = pd.read_csv("offers.csv", sep=';')

    min_price = min(df["Price"])
    max_price = max(df["Price"])
    min_year = min(df["Year"])
    max_year = max(df["Year"])
    min_mil = int(min(df["Mileage"]))
    max_mil = int(max(df["Mileage"]))
    min_power = int(min(df["Power"]))
    max_power = int(max(df["Power"]))

    # I. Filters
    # 1. Price
    price_output = "Cena: "
    price_style_dict = {"width": "15%", "position": "absolute", "left": "1%",
                        "top": "2%", "height": "10%", "font-size": 18,
                        "font-family": "Cambria"}
    error_message = "Minimalna cena jest większa od maksymalnej"

    price_output, price_min_limit, price_max_limit \
        = input_hint(price_output, price_style_dict, price_input_1,
                     price_input_2, min_price, max_price, error_message, "zł",
                     1)

    ph_1_1 = "Min. cena (od {})".format(min_price)
    ph_1_2 = "Max. cena (od {})".format(max_price)
    ph_2_1 = "Min. rok produkcji (od {})".format(min_year)
    ph_2_2 = "Max. rok produkcji (od {})".format(max_year)
    ph_3_1 = "Min. przebieg (od {})".format(min_mil)
    ph_3_2 = "Max. przebieg (od {})".format(max_mil)
    ph_4_1 = "Min. moc (od {})".format(min_power)
    ph_4_2 = "Max. moc (od {})".format(max_power)

    # 2. Production year
    year_output = "Rok produkcji: "
    year_style_dict = {"width": "15%", "position": "absolute", "left": "18%",
                       "top": "2%", "height": "10%", "font-size": 18,
                       "font-family": "Cambria"}
    error_message = "Minimalny rok produkcji jest większy od maksymalnego"

    year_output, year_min_limit, year_max_limit \
        = input_hint(year_output, year_style_dict, year_input_1,
                     year_input_2, min_year, max_year, error_message, "", 0)

    # 3. Mileage
    mileage_output = "Przebieg: "
    mileage_style_dict = {"width": "15%", "position": "absolute",
                          "left": "37%", "top": "2%", "height": "10%",
                          "font-size": 18, "font-family": "Cambria"}
    error_message = "Minimalny przebieg jest większy od maksymalnego"

    mileage_output, mileage_min_limit, mileage_max_limit \
        = input_hint(mileage_output, mileage_style_dict, mileage_input_1,
                     mileage_input_2, min_mil, max_mil, error_message, "km",
                     1)

    # 4. Power
    power_output = "Moc: "
    power_style_dict = {"width": "15%", "position": "absolute",
                        "left": "56%", "top": "2%", "height": "10%",
                        "font-size": 18, "font-family": "Cambria"}
    error_message = "Minimalna moc jest większa od maksymalnej"

    power_output, power_min_limit, power_max_limit \
        = input_hint(power_output, power_style_dict, power_input_1,
                     power_input_2, min_power, max_power, error_message, "KM",
                     1)

    # 5. Fuel
    fuel_output = "Paliwo:"

    # 6. Brand
    brand_output = "Marka: "
    if brand_input:
        brand_output += brand_input

    # 7. Number of offers
    if price_input_1:
        df = df[df["Price"] >= int(price_input_1)]
    if price_input_2:
        df = df[df["Price"] <= int(price_input_2)]
    if year_input_1:
        df = df[df["Year"] >= int(year_input_1)]
    if year_input_2:
        df = df[df["Year"] <= int(year_input_2)]
    if mileage_input_1:
        df = df[df["Mileage"] >= int(mileage_input_1)]
    if mileage_input_2:
        df = df[df["Mileage"] <= int(mileage_input_2)]
    if power_input_1:
        df = df[df["Power"] >= int(power_input_1)]
    if power_input_2:
        df = df[df["Power"] <= int(power_input_2)]

    df = df[df["Fuel"].isin(fuel_input)]
    if brand_input != "wszystkie":
        df = df[df["Brand"] == brand_input]

    n_of_offs = str(len(df))
    n_of_offs_out = "Wybrano ofert: " + n_of_offs

    # II. Plots preparation

    # 1. Visibility
    base_style_dict = {"left": "0%", "width": "60%"}
    style_0_1 = base_style_dict.copy()
    style_0_2 = base_style_dict.copy()
    style_0_3 = base_style_dict.copy()
    style_1_1 = base_style_dict.copy()
    style_1_2 = base_style_dict.copy()
    style_1_3 = base_style_dict.copy()

    # 2. Dropdown options
    numerical_labels = ["Cena", "Przebieg", "Moc"]
    numerical_values = ["Price", "Mileage", "Power"]
    categorical_labels = ["Rok", "Paliwo", "Marka"]
    categorical_values = ["Year", "Fuel", "Brand"]

    out_0_1, out_0_2, out_0_3, style_0_1, style_0_2, style_0_3 \
        = get_dropdown_options(in_0_0, style_0_1, style_0_2, style_0_3,
                               numerical_labels, categorical_labels,
                               numerical_values, categorical_values)
    out_1_1, out_1_2, out_1_3, style_1_1, style_1_2, style_1_3 \
        = get_dropdown_options(in_1_0, style_1_1, style_1_2, style_1_3,
                               numerical_labels, categorical_labels,
                               numerical_values, categorical_values)

    # III. Plots creation
    plot_type_1 = get_plot_type(in_0_0, in_0_1, in_0_2)
    plot_type_2 = get_plot_type(in_1_0, in_1_1, in_1_2)

    fig_1 = create_plot(plot_type_1, df, in_0_1, in_0_2, in_0_3)
    fig_2 = create_plot(plot_type_2, df, in_1_1, in_1_2, in_1_3)

    # IV. Link search
    if not link_search_in:
        link_search_out = ""
    else:
        try:
            link_search_out = df["Link"].loc[int(link_search_in)]
        except:
            link_search_out = "Błędny numer id"

    return [price_output, price_style_dict, ph_1_1, ph_1_2, year_output,
            year_style_dict, ph_2_1, ph_2_2, mileage_output,
            mileage_style_dict, ph_3_1, ph_3_2, power_output,
            power_style_dict, ph_4_1, ph_4_2, fuel_output, brand_output,
            n_of_offs_out, out_0_1, out_0_2, out_0_3, out_1_1, out_1_2,
            out_1_3, style_0_1, style_0_2, style_0_3, style_1_1, style_1_2,
            style_1_3, fig_1, fig_2, link_search_out]
