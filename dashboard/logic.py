import pandas as pd

from funcs_filters import *
from funcs_plotsettings import *
from funcs_plots import *


def backend(price_input_1, price_input_2, year_input_1, year_input_2,
            mileage_input_1, mileage_input_2, power_input_1, power_input_2,
            fuel_input, brand_input, in_0_0, in_0_1, in_0_2, in_0_3, in_1_0,
            in_1_1, in_1_2, in_1_3, link_search_in):

    # I. Filters
    # 1. Price
    min_price = 2000
    max_price = 80000
    price_output = "Cena: "
    price_style_dict = {"width": "15%", "position": "absolute", "left": "1%",
                        "top": "13%", "height": "10%", "font-size": 18,
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
    year_style_dict = {"width": "15%", "position": "absolute", "left": "18%",
                       "top": "13%", "height": "10%", "font-size": 18,
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
                          "left": "37%", "top": "13%", "height": "10%",
                          "font-size": 18, "font-family": "Cambria"}
    error_message = "Minimalny przebieg jest większy od maksymalnego"

    mileage_output, mileage_min_limit, mileage_max_limit \
        = input_hint(mileage_output, mileage_style_dict, mileage_input_1,
                     mileage_input_2, min_mil, max_mil, error_message, "km",
                     1)

    # 4. Power
    min_power = 80
    max_power = 300
    power_output = "Moc: "
    power_style_dict = {"width": "15%", "position": "absolute",
                        "left": "56%", "top": "13%", "height": "10%",
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
    df = pd.read_csv("offers.csv", sep=";")

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
    out_0_1, out_0_2, out_0_3, out_1_1, out_1_2, out_1_3 \
        = [], [], [], [], [], []
    numerical_labels = ["Cena", "Przebieg", "Moc"]
    categorical_labels = ["Rok", "Paliwo", "Marka"]
    numerical_values = ["Price", "Mileage", "Power"]
    categorical_values = ["Year", "Fuel", "Brand"]

    if in_0_0 == 1:
        out_0_1 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
        out_0_2 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
        out_0_3 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
    elif in_0_0 == 2:
        out_0_1 = [{"label": lab, "value": val}
                   for lab, val in zip(categorical_labels, categorical_values)]
        out_0_2 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
        out_0_3 = []
        style_0_3["display"] = "none"

    elif in_0_0 == 3:
        out_0_1 = []
        out_0_2 = []
        out_0_3 = [{"label": lab, "value": val}
                   for lab, val in zip(numerical_labels, numerical_values)]
        style_0_1["display"] = "none"
        style_0_2["display"] = "none"

    # III. Plots creation
    plot_type_1 = None
    if in_0_0 == 1:
        if in_0_1 and in_0_2:
            plot_type_1 = 1  # scatterplot
        elif bool(in_0_1) != bool(in_0_2):
            plot_type_1 = 2  # histogram
    elif in_0_0 == 2:
        if in_0_1 and in_0_2:
            plot_type_1 = 3  # boxplot
        elif in_0_1 and not in_0_2:
            plot_type_1 = 4  # barplot
    elif in_0_0 == 3:
        plot_type_1 = 5  # map

    plot_type_2 = in_1_0

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

    return [price_output, price_style_dict, year_output, year_style_dict,
            mileage_output, mileage_style_dict, power_output, power_style_dict,
            fuel_output, brand_output, n_of_offs_out, out_0_1,
            out_0_2, out_0_3, out_1_1, out_1_2, out_1_3, style_0_1, style_0_2,
            style_0_3, style_1_1, style_1_2, style_1_3, fig_1, fig_2,
            link_search_out]
