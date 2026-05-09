import random

def classify_uploaded_disaster():

    disaster_categories = [
        "Flood",
        "Fire",
        "Landslide",
        "Road Block",
        "Accident",
        "Fallen Tree"
    ]

    prediction = random.choice(disaster_categories)

    return prediction