import streamlit as st

import pandas as pd

import plotly.express as px

from database import cursor

from styles import load_css

load_css()

st.title("📊 Rescue SL Analytics Dashboard")

st.markdown("---")

cursor.execute(
    """
    SELECT

        disaster_type,
        COUNT(*)

    FROM reports

    GROUP BY disaster_type
"""
)

data = cursor.fetchall()

disaster_dataframe = pd.DataFrame(

    data,

    columns=[
        "Disaster Type",
        "Count"
    ]
)

bar_chart = px.bar(

    disaster_dataframe,

    x="Disaster Type",

    y="Count",

    title="Disaster Distribution Analysis"
)

st.plotly_chart(
    bar_chart,
    use_container_width=True
)

st.markdown("---")

cursor.execute(
    """
    SELECT

        district,
        COUNT(*)

    FROM reports

    GROUP BY district
"""
)

district_data = cursor.fetchall()

district_dataframe = pd.DataFrame(

    district_data,

    columns=[
        "District",
        "Count"
    ]
)

pie_chart = px.pie(

    district_dataframe,

    names="District",

    values="Count",

    title="District Wise Disaster Distribution"
)

st.plotly_chart(
    pie_chart,
    use_container_width=True
)

st.markdown("---")

cursor.execute(
    """
    SELECT

        severity,
        COUNT(*)

    FROM reports

    GROUP BY severity
"""
)

severity_data = cursor.fetchall()

severity_dataframe = pd.DataFrame(

    severity_data,

    columns=[
        "Severity",
        "Count"
    ]
)

severity_chart = px.bar(

    severity_dataframe,

    x="Severity",

    y="Count",

    title="Severity Level Analysis"
)

st.plotly_chart(
    severity_chart,
    use_container_width=True
)