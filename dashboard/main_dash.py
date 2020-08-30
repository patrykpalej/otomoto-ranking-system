import dash
import pandas as pd
import plotly.express as px
from datetime import datetime
import matplotlib.pyplot as plt
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from funcs import *
from layout import frontend
from logic import backend


app = dash.Dash(__name__)

app.layout = frontend()


@app.callback(
     [Output(component_id='id_o1', component_property='text'),
      Output(component_id='id_o2', component_property='text')],

     [Input(component_id='id1', component_property='text'),
      Input(component_id='id2', component_property='text')]
)
def update_graphs(backend_input1, backend_input2):

    [backend_output1, backend_output2] = backend(backend_input1,
                                                 backend_input2)

    return [backend_output1, backend_output2]


if __name__ == '__main__':
    app.run_server(debug=True)
