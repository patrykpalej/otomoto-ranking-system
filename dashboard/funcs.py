import plotly.graph_objects as go
from plotly.subplots import make_subplots


def input_hint(hint_text, style_dict, input_1, input_2, min_limit, max_limit,
               error_message, unit):

    if input_1 and input_2:
        hint_text += input_1 + "{} - ".format(unit) + input_2 + unit

        if int(input_1) < min_limit or int(input_2) > max_limit:
            hint_text = "Wybierz z zakresu {}{} - {}{}"\
                .format(str(int(min_limit)), unit, str(int(max_limit)), unit)
            style_dict["color"] = "red"

        if int(input_1) > int(input_2):
            hint_text = error_message
            style_dict["color"] = "red"

    return hint_text


def draw_plot(backend_input1):
    plot = make_subplots()

    if 1 in backend_input1:
        plot.add_trace(go.Scatter(x=[1, 2], y=[3, 4]))

    if 2 in backend_input1:
        plot.add_trace(go.Scatter(x=[1, 2], y=[4, 3],
                       marker=dict(color="orange")))

    return plot
