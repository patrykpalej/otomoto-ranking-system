import dash_core_components as dcc
import dash_html_components as html


def frontend(brand_options):

    layout_ = html.Div([
        html.H1("Oferty samochodów na otomoto.pl",
                style={"text-align": "center", "fontSize": "50px",
                       "margin": "0", "font-family": "Cambria"}),

        # 1. Filters
        # a) Price range
        html.Div(id="price_output", children=[], style={}),

        html.Div([
            dcc.Input(id="price_input_1", type="text",
                      placeholder="Cena min. (od 2000)",
                      style={"height": "20px"}),

            dcc.Input(id="price_input_2", type="text",
                      placeholder="Cena max. (do 80 000)",
                      style={"height": "20px"}),
        ], style={"display": "grid", "grid-row-gap": "10%", "width": "12%",
                  "position": "absolute", "top": "20%", "left": "1%"}),

        # b) Production year
        html.Div(id="year_output", children=[], style={}),

        html.Div([
            dcc.Input(id="year_input_1", type="text",
                      placeholder="Min. rok produkcji (od 2000)",
                      style={"height": "20px"}),

            dcc.Input(id="year_input_2", type="text",
                      placeholder="Max. rok produkcji (do 2019)",
                      style={"height": "20px"}),
        ], style={"display": "grid", "grid-row-gap": "10%", "width": "12%",
                  "position": "absolute", "top": "20%", "left": "18%"}),

        # c) Mileage
        html.Div(id="mileage_output", children=[], style={}),

        html.Div([
            dcc.Input(id="mileage_input_1", type="text",
                      placeholder="Min. przebieg (od 10k)",
                      style={"height": "20px"}),

            dcc.Input(id="mileage_input_2", type="text",
                      placeholder="Max. przebieg (do 1M)",
                      style={"height": "20px"}),
        ], style={"display": "grid", "grid-row-gap": "10%", "width": "12%",
                  "position": "absolute", "top": "20%", "left": "37%"}),

        # d) Power
        html.Div(id="power_output", children=[], style={}),

        html.Div([
            dcc.Input(id="power_input_1", type="text",
                      placeholder="Min. moc (od 10k)",
                      style={"height": "20px"}),

            dcc.Input(id="power_input_2", type="text",
                      placeholder="Max. moc (do 1M)",
                      style={"height": "20px"}),
        ], style={"display": "grid", "grid-row-gap": "10%", "width": "12%",
                  "position": "absolute", "top": "20%", "left": "56%"}),

        # e) Fuel
        html.Div(id="fuel_output", children=[],
                 style={"left": "72%", "position": "absolute", "top": "13%",
                        "height": "10%", "font-size": 18, "font-family":
                            "Cambria"}),

        dcc.Checklist(id="fuel_input", options=[
            {"label": "Benzyna", "value": "Benzyna"},
            {"label": "Benzyna + LPG", "value": "Benzyna+LPG"},
            {"label": "Diesel", "value": "Diesel"}],
                      value=["Benzyna", "Benzyna+LPG", "Diesel"],
                      style={"top": "20%", "left": "72%", "display": "grid",
                             "width": "30%", "position": "absolute"}),

        # f) Brand
        html.Div(id="brand_output", children=[],
                 style={"left": "82%", "position": "absolute", "top": "13%",
                        "height": "10%", "font-size": 18, "font-family":
                            "Cambria"}),

        html.Div(children=[
            dcc.Dropdown(id="brand_input", options=brand_options,
                         value="wszystkie", placeholder="Wybierz markę",
                         style={"top": "20%", "width": "100%",
                                "position": "absolute"})],
                 style={"top": "20%", "left": "82%", "display": "block-inline",
                        "width": "10%", "position": "absolute"}),

        # g) Number of offers left
        html.Div(id="n_of_offs_out", children=[],
                 style={"position": "absolute", "top": "32%", "left": "45%",
                        "height": "10%", "font-size": 18, "font-family":
                        "Cambria", 'justifyContent': 'center'}),

        # 2. Plots settings
        html.Div([
            dcc.Dropdown(options=[],
                         placeholder="",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="",
                         style={"left": "0%", "width": "60%"})
        ],
            style={"left": "0%", "top": "36%", "position": "absolute",
                   "display": "flex", "flex-direction": "row",
                   "width": "50%", "justify-content": "flex-start"}
        ),

        # html.Div([
        #     dcc.Dropdown(style={"width": "12%", "left": "0", "top": "40%"}),
        #     dcc.Dropdown(style={"width": "12%", "left": "12%", "top": "40%"}),
        #     dcc.Dropdown(style={"width": "12%", "left": "24%", "top":
        #         "40%"}), #],
            # style={"left": "0%", "top": "40%", "position": "absolute",
            #        "width": "45%"}
        # ),


        # 3. Plots
        dcc.Graph(id="fig_1", figure={},
                  style={"width": "50%", "height": "54%", "bottom": "1%",
                         "position": "absolute", "left": "0%", "top": "46%"}),

        dcc.Graph(id="fig_2", figure={},
                  style={"width": "50%", "height": "64%", "bottom": "1%",
                         "position": "absolute", "left": "50%", "top": "46%"})

    ])

    return layout_
