import dash
from dash.dependencies import Input, Output

from layout import frontend
from logic import backend


app = dash.Dash(__name__)

app.layout = frontend()


@app.callback(
     [Output(component_id='output_1', component_property='figure'),
      Output(component_id='output_2', component_property='children')],

     [Input(component_id='input_1', component_property='value'),
      Input(component_id='input_2', component_property='value')]
)
def update_graphs(backend_input1, backend_input2):

    [backend_output1, backend_output2] = backend(backend_input1,
                                                 backend_input2)

    return [backend_output1, backend_output2]


if __name__ == '__main__':
    app.run_server(debug=True)
