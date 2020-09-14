import plotly.express as px


def create_plot(plot_type, df, x, y, color):

    if plot_type == 1:
        fig = create_scatterplot(df, x, y, color)
    elif plot_type == 2:
        fig = create_histogram(df, x, y)
    elif plot_type == 3:
        fig = create_boxplot(df, x, y)
    elif plot_type == 4:
        fig = create_barplot(df, x)
    elif plot_type == 5:
        fig = create_map(df, color)
    else:
        fig = px.line()

    return fig


def create_scatterplot(df, x, y, color):
    fig = px.scatter(df, x=x, y=y, color=color, text=df.index,
                     color_continuous_scale="jet")
    fig.for_each_trace(lambda t: t.update(mode="markers"))

    return fig


def create_histogram(df, x, y):
    if x:
        fig = px.histogram(df[x])
    else:
        fig = px.histogram(df[y])

    return fig


def create_boxplot(df, x, y):
    fig = px.box(df, x=x, y=y)

    return fig


def create_barplot(df, x):
    df_group = df.groupby([x]).count()["id"].sort_values(ascending=False)
    if x == "Brand":
        df_group = df_group[:10]

    fig = px.bar(x=df_group.index, y=df_group)

    return fig


def create_map(df, color):

    fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude",
                            color=color, zoom=5, color_continuous_scale="jet",
                            mapbox_style="carto-positron", text=df.index)
    fig.for_each_trace(lambda t: t.update(mode="markers"))

    return fig


def get_plot_type(in_0, in_1, in_2):
    plot_type = None
    if in_0 == 1:
        if in_1 and in_2:
            plot_type = 1  # scatterplot
        elif bool(in_1) != bool(in_2):
            plot_type = 2  # histogram
    elif in_0 == 2:
        if in_1 and in_2:
            plot_type = 3  # boxplot
        elif in_1 and not in_2:
            plot_type = 4  # barplot
    elif in_0 == 3:
        plot_type = 5  # map

    return plot_type
