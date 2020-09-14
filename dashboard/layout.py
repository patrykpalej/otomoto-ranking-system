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
            dcc.Dropdown(options=[{"label": "Scatterplot", "value": 1},
                                  {"label": "Boxplot", "value": 2},
                                  {"label": "Mapa", "value": 3}],
                         placeholder="Wykres", id="drop_0_0",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="Oś X", id="drop_0_1",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="Oś Y", id="drop_0_2",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="Kolor", id="drop_0_3",
                         style={"left": "0%", "width": "60%"})
        ],
            style={"left": "5%", "top": "36%", "position": "absolute",
                   "display": "flex", "flex-direction": "row",
                   "width": "40%", "justify-content": "flex-start"}
        ),

        html.Div([
            dcc.Dropdown(options=[{"label": "Scatterplot", "value": 1},
                                  {"label": "Boxplot", "value": 2},
                                  {"label": "Mapa", "value": 3}],
                         placeholder="Wykres", id="drop_1_0",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="Oś X", id="drop_1_1",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="Oś Y", id="drop_1_2",
                         style={"left": "0%", "width": "60%"}),
            dcc.Dropdown(options=[],
                         placeholder="Kolor", id="drop_1_3",
                         style={"left": "0%", "width": "60%"})
        ],
            style={"left": "60%", "top": "36%", "position": "absolute",
                   "display": "flex", "flex-direction": "row",
                   "width": "40%", "justify-content": "flex-start"}
        ),


        # 3. Plots
        dcc.Graph(id="fig_1", figure={},
                  style={"width": "40%", "height": "60%", "position":
                         "absolute", "left": "1%", "top": "42%"}),

        dcc.Graph(id="fig_2", figure={},
                  style={"width": "40%", "height": "60%", "position":
                         "absolute", "left": "55%", "top": "42%"}),


        # 4. Link search
        html.Div(children=["Wpisz id oferty aby otrzymać link:"],
                 style={"position": "absolute", "left": "43%", "top": "70%",
                        "font-family": "Cambria", "width": "10%",
                        "height": "5%"}),
        dcc.Input(id="link_search_in",
                  style={"position": "absolute", "left": "43%", 
                         "top": "76%", "width": "8%"}),
        html.Div(id="link_search_out", children=[],
                 style={"position": "absolute", "left": "43%", "top": "80%",
                        "width": "12%"})

    ])

    return layout_
