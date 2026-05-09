import folium

def create_disaster_marker(
    map_object,
    latitude,
    longitude,
    disaster_type,
    district
):

    marker_color = "blue"

    if disaster_type == "Flood":
        marker_color = "blue"

    elif disaster_type == "Fire":
        marker_color = "red"

    elif disaster_type == "Landslide":
        marker_color = "orange"

    elif disaster_type == "Accident":
        marker_color = "darkred"

    folium.Marker(
        [latitude, longitude],
        popup=f"{disaster_type} - {district}",
        icon=folium.Icon(color=marker_color)
    ).add_to(map_object)