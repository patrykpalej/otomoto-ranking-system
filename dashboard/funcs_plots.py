import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_plot(plot_type, graph_id, data):

    fig = px.line()

    if plot_type == 0:
        fig = create_scatter_plot(data)
    elif plot_type == 1:
        fig = create_bar_plot(data)
    elif plot_type == 2:
        fig = create_map(data)

    return fig


def create_scatter_plot(data):

    fig = px.line([0, 1], [0, 2])
    fig = px.line()

    return fig


def create_bar_plot(data):

    fig = px.line([0, 1], [0, 2])
    fig = px.line()

    return fig


def create_map(data):

    fig = px.line([0, 1], [0, 2])

    return fig
