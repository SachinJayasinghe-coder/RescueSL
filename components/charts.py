import plotly.express as px

def create_bar_chart(dataframe):

    figure = px.bar(
        dataframe,
        x="Disaster Type",
        y="Count",
        title="Disaster Statistics"
    )

    return figure


def create_pie_chart(dataframe):

    figure = px.pie(
        dataframe,
        names="District",
        values="Count",
        title="District Report Distribution"
    )

    return figure