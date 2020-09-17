import dash
import pandas as pd
from dash.dependencies import Input, Output

from layout import frontend
from logic import backend


app = dash.Dash(__name__)

# 0. Prepare
df = pd.read_csv("offers.csv", sep=';', usecols=["Brand"])
common_brands = df["Brand"].value_counts().index[:10]
brand_options = [{"label": "Wszystkie", "value": "wszystkie"}]
for x in common_brands:
    brand_options.append({"label": x, "value": x})

# 1. Frontend
app.layout = frontend(brand_options)


# 2. Backend
@app.callback(
     [Output(component_id="price_output", component_property="children"),
      Output(component_id="price_output", component_property="style"),
      Output(component_id="year_output", component_property="children"),
      Output(component_id="year_output", component_property="style"),
      Output(component_id="mileage_output", component_property="children"),
      Output(component_id="mileage_output", component_property="style"),
      Output(component_id="power_output", component_property="children"),
      Output(component_id="power_output", component_property="style"),
      Output(component_id="fuel_output", component_property="children"),
      Output(component_id="brand_output", component_property="children"),
      Output(component_id="n_of_offs_out", component_property="children"),
      Output(component_id="drop_0_1", component_property="options"),
      Output(component_id="drop_0_2", component_property="options"),
      Output(component_id="drop_0_3", component_property="options"),
      Output(component_id="drop_1_1", component_property="options"),
      Output(component_id="drop_1_2", component_property="options"),
      Output(component_id="drop_1_3", component_property="options"),
      Output(component_id="drop_0_1", component_property="style"),
      Output(component_id="drop_0_2", component_property="style"),
      Output(component_id="drop_0_3", component_property="style"),
      Output(component_id="drop_1_1", component_property="style"),
      Output(component_id="drop_1_2", component_property="style"),
      Output(component_id="drop_1_3", component_property="style"),
      Output(component_id="fig_1", component_property="figure"),
      Output(component_id="fig_2", component_property="figure"),
      Output(component_id="link_search_out", component_property="children")],

     [Input(component_id="price_input_1", component_property="value"),
      Input(component_id="price_input_2", component_property="value"),
      Input(component_id="year_input_1", component_property="value"),
      Input(component_id="year_input_2", component_property="value"),
      Input(component_id="mileage_input_1", component_property="value"),
      Input(component_id="mileage_input_2", component_property="value"),
      Input(component_id="power_input_1", component_property="value"),
      Input(component_id="power_input_2", component_property="value"),
      Input(component_id="fuel_input", component_property="value"),
      Input(component_id="brand_input", component_property="value"),
      Input(component_id="drop_0_0", component_property="value"),
      Input(component_id="drop_0_1", component_property="value"),
      Input(component_id="drop_0_2", component_property="value"),
      Input(component_id="drop_0_3", component_property="value"),
      Input(component_id="drop_1_0", component_property="value"),
      Input(component_id="drop_1_1", component_property="value"),
      Input(component_id="drop_1_2", component_property="value"),
      Input(component_id="drop_1_3", component_property="value"),
      Input(component_id="link_search_in", component_property="value")]
)
def update_dashboard(price_input_1, price_input_2, year_input_1, year_input_2,
                     mileage_input_1, mileage_input_2, power_input_1,
                     power_input_2, fuel_input, brand_input, in_0_0, in_0_1,
                     in_0_2, in_0_3, in_1_0, in_1_1, in_1_2, in_1_3,
                     link_search_in):

    [price_output, price_style_dict, year_output, year_style_dict,
     mileage_output, mileage_style_dict, power_output, power_style_dict,
     fuel_output, brand_output, n_of_offs_out, out_0_1, out_0_2,
     out_0_3, out_1_1, out_1_2, out_1_3, style_0_1, style_0_2, style_0_3,
     style_1_1, style_1_2, style_1_3, fig_1, fig_2, link_search_out] \
        = backend(price_input_1, price_input_2, year_input_1, year_input_2,
                  mileage_input_1, mileage_input_2, power_input_1,
                  power_input_2, fuel_input, brand_input, in_0_0, in_0_1,
                  in_0_2, in_0_3, in_1_0, in_1_1, in_1_2, in_1_3,
                  link_search_in)

    return [price_output, price_style_dict, year_output, year_style_dict,
            mileage_output, mileage_style_dict, power_output,
            power_style_dict, fuel_output, brand_output, n_of_offs_out,
            out_0_1, out_0_2, out_0_3, out_1_1, out_1_2,
            out_1_3, style_0_1, style_0_2, style_0_3, style_1_1, style_1_2,
            style_1_3, fig_1, fig_2, link_search_out]


if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
