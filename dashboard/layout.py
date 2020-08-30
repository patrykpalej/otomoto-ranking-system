from datetime import datetime
import dash_core_components as dcc
import dash_html_components as html


def frontend():
    layout_ = html.Div([
        html.H1("Kursy walut",
                style={"text-align": "center", "fontSize": "50px",
                       "margin": "0"}, id="id1"),

        html.H2("Opcje wizualizacji", id="id2",
                style={"top": "18%", "left": "40%", "position": "absolute"}),

        html.H1("Kursy walut",
                style={"text-align": "center", "fontSize": "50px",
                       "margin": "0"}, id="id_o1"),
        html.H1("Kursy walut",
                style={"text-align": "center", "fontSize": "50px",
                       "margin": "0"}, id="id_o2")

    ])

    return layout_
