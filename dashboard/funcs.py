import plotly.graph_objects as go
from plotly.subplots import make_subplots


def funcs_used_in_logic_section():
    pass


def draw_plot(backend_input1):
    plot = make_subplots()

    if 1 in backend_input1:
        plot.add_trace(go.Scatter(x=[1, 2], y=[3, 4]))

    if 2 in backend_input1:
        plot.add_trace(go.Scatter(x=[1, 2], y=[4, 3],
                       marker=dict(color="black")))

    return plot
