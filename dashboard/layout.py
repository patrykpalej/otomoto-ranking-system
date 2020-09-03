import dash_core_components as dcc
import dash_html_components as html


def frontend():
    layout_ = html.Div([
        html.H1("Oferty samochodów na otomoto.pl",
                style={"text-align": "center", "fontSize": "50px",
                       "margin": "0", "font-family": "Cambria"}),

        # 1. Price range
        html.Div(id="price_output", children=[],
                 style={"width": "15%", "position": "absolute", "left": "5%",
                        "top": "10%", "height": "10%", "font-size": 18,
                        "font-family": "Cambria"}),

        html.Div([
            dcc.Input(id="price_input_1", type="text",
                      placeholder="Cena min. (od 2000)",
                      style={"height": "20px", "width": "170px"}),

            dcc.Input(id="price_input_2", type="text",
                      placeholder="Cena max. (do 80 000)",
                      style={"height": "20px", "width": "170px"}),
        ], style={"display": "grid", "grid-row-gap": "20px",
                  "position": "absolute", "top": "17%", "left": "5%"}),

        # 2. Production year
        html.Div(id="year_output", children=[],
                 style={"width": "20%", "position": "absolute", "left": "20%",
                        "top": "10%", "height": "1%", "font-size": 18,
                        "font-family": "Cambria"}),

        html.Div([
            dcc.Input(id="year_input_1", type="text",
                      placeholder="Min. rok produkcji (od 2000)",
                      style={"height": "20px", "width": "170px"}),

            dcc.Input(id="year_input_2", type="text",
                      placeholder="Max. rok produkcji (do 2019)",
                      style={"height": "20px", "width": "170px"}),
        ], style={"display": "grid", "grid-row-gap": "20px",
                  "position": "absolute", "top": "17%", "left": "20%"}),

        # 3. Mileage
        html.Div(id="mileage_output", children=[],
                 style={"width": "20%", "position": "absolute", "left": "35%",
                        "top": "10%", "height": "1%", "font-size": 18,
                        "font-family": "Cambria"}),

        html.Div([
            dcc.Input(id="mileage_input_1", type="text",
                      placeholder="Min. przebieg (od 10k)",
                      style={"height": "20px", "width": "170px"}),

            dcc.Input(id="mileage_input_2", type="text",
                      placeholder="Max. przebieg (do 1M)",
                      style={"height": "20px", "width": "170px"}),
        ], style={"display": "grid", "grid-row-gap": "20px",
                  "position": "absolute", "top": "17%", "left": "35%"})

    ])

    return layout_
