import streamlit as st

import folium

from streamlit_folium import st_folium

from database import cursor

from styles import load_css

load_css()

st.title("🗺️ Live Disaster Map")

st.markdown("---")

map_object = folium.Map(

    location=[7.8731, 80.7718],

    zoom_start=7
)

cursor.execute(
    """
    SELECT

        disaster_type,
        latitude,
        longitude,
        district,
        severity

    FROM reports
"""
)

reports = cursor.fetchall()

for report in reports:

    disaster_type = report[0]

    latitude = report[1]

    longitude = report[2]

    district = report[3]

    severity = report[4]

    marker_color = "blue"

    if disaster_type == "Flood":

        marker_color = "blue"

    elif disaster_type == "Fire":

        marker_color = "red"

    elif disaster_type == "Landslide":

        marker_color = "orange"

    elif disaster_type == "Road Block":

        marker_color = "purple"

    elif disaster_type == "Accident":

        marker_color = "darkred"

    folium.Marker(

        [latitude, longitude],

        popup=f"""
        Disaster Type: {disaster_type}

        District: {district}

        Severity: {severity}
        """,

        icon=folium.Icon(
            color=marker_color
        )

    ).add_to(map_object)

st_folium(

    map_object,

    width=1400,

    height=700
)