import streamlit as st

import os

import datetime

from PIL import Image

from database import connection
from database import cursor

from utils import generate_ai_confidence

from styles import load_css

load_css()

st.title("🚨 Report Disaster")

st.markdown("---")

disaster_type = st.selectbox(

    "Select Disaster Type",

    [
        "Flood",
        "Fire",
        "Landslide",
        "Road Block",
        "Fallen Tree",
        "Accident"
    ]
)

description = st.text_area(
    "Disaster Description"
)

district = st.selectbox(

    "Select District",

    [
        "Colombo",
        "Gampaha",
        "Kalutara",
        "Kandy",
        "Galle",
        "Kurunegala"
    ]
)

severity = st.selectbox(

    "Select Severity Level",

    [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]
)

latitude = st.number_input(
    "Latitude",
    format="%.6f"
)

longitude = st.number_input(
    "Longitude",
    format="%.6f"
)

uploaded_file = st.file_uploader(
    "Upload Disaster Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Disaster Image",
        use_container_width=True
    )

if st.button("Submit Disaster Report"):

    image_path = ""

    if uploaded_file is not None:

        save_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(save_path, "wb") as file:

            file.write(
                uploaded_file.getbuffer()
            )

        image_path = save_path

    ai_confidence = generate_ai_confidence()

    cursor.execute(
        """
        INSERT INTO reports(

            user_id,
            disaster_type,
            description,
            image_path,
            district,
            latitude,
            longitude,
            status,
            severity,
            verification_count,
            ai_confidence,
            created_at

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
        """,

        (
            1,
            disaster_type,
            description,
            image_path,
            district,
            latitude,
            longitude,
            "ACTIVE",
            severity,
            0,
            ai_confidence,
            str(datetime.datetime.now())
        )
    )

    connection.commit()

    st.success(
        "Disaster Report Submitted Successfully"
    )

    st.info(
        f"AI Verification Confidence: {ai_confidence}%"
    )