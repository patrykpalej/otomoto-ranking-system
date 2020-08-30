import dash_core_components as dcc
import dash_html_components as html


def frontend():
    layout_ = html.Div([
        html.H1("Dashboard title",
                style={"text-align": "center", "fontSize": "50px",
                       "margin": "0"}),

        dcc.Checklist(id="input_1", value=[1], options=[
            {"label": "Hello", "value": 1},
            {"label": "World", "value": 2}],
                      style={"width": "10%", "position": "absolute",
                             "display": "grid", "left": "10%", "top": "25%",
                             "height": "12%"}),
        
        dcc.RadioItems(id="input_2", options=[
            {"label": "This", "value": 1},
            {"label": "is a", "value": 2},
            {"label": "simple", "value": 3},
            {"label": "dashboard", "value": 4}], value=2,
                       style={"width": "10%", "position": "absolute",
                              "display": "grid", "left": "60%", "top": "25%",
                              "height": "12%"}),

        dcc.Graph(
            style={"width": "40%", "height": "50%", "position": "absolute",
                   "left": "10%", "top": "40%"}, id="output_1", figure={}),

        html.Div(id="output_2", children=[],
                 style={"top": "50%", "left": "60%", "position": "absolute",
                        "border": "black solid 2px", "padding": "4px"})
    ])

    return layout_
