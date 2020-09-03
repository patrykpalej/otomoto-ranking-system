import dash
from dash.dependencies import Input, Output

from layout import frontend
from logic import backend


app = dash.Dash(__name__)

app.layout = frontend()


@app.callback(
     [Output(component_id="price_output", component_property="children"),
      Output(component_id='price_output', component_property="style"),
      Output(component_id="year_output", component_property="children"),
      Output(component_id='year_output', component_property="style"),
      Output(component_id="mileage_output", component_property="children"),
      Output(component_id='mileage_output', component_property="style")],

     [Input(component_id="price_input_1", component_property="value"),
      Input(component_id="price_input_2", component_property="value"),
      Input(component_id="year_input_1", component_property="value"),
      Input(component_id="year_input_2", component_property="value"),
      Input(component_id="mileage_input_1", component_property="value"),
      Input(component_id="mileage_input_2", component_property="value")]
)
def update_dashboard(price_input_1, price_input_2, year_input_1, year_input_2,
                     mileage_input_1, mileage_input_2):

    [price_output, price_style_dict, year_output, year_style_dict,
     mileage_output, mileage_style_dict] \
        = backend(price_input_1, price_input_2, year_input_1, year_input_2,
                  mileage_input_1, mileage_input_2)

    return [price_output, price_style_dict, year_output, year_style_dict,
            mileage_output, mileage_style_dict]


if __name__ == '__main__':
    app.run_server(debug=True)
