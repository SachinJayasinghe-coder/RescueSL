import streamlit as st
import pandas as pd
from database import connection, cursor
from styles import load_css

load_css()

st.title("🤝 Volunteer Coordination Center")

st.markdown("""
This section allows citizens to register as emergency volunteers
during disasters and emergency situations.
""")

st.markdown("---")

st.subheader("📝 Register As Volunteer")

name = st.text_input("Full Name")

district = st.selectbox(
    "District",
    [
        "Colombo",
        "Gampaha",
        "Kalutara",
        "Kandy",
        "Galle",
        "Kurunegala"
    ]
)

contact_number = st.text_input("Contact Number")

availability = st.selectbox(
    "Availability",
    [
        "Available Full Time",
        "Available Part Time",
        "Emergency Only"
    ]
)

skills = st.text_area(
    "Skills / Resources",
    placeholder="First Aid, Transport, Food Distribution, Rescue Support..."
)

if st.button("Register Volunteer"):

    cursor.execute(
        """
        INSERT INTO volunteers(
            user_id,
            district,
            availability,
            contact_number,
            skills
        )
        VALUES(?,?,?,?,?)
        """,
        (
            1,
            district,
            availability,
            contact_number,
            skills
        )
    )

    connection.commit()

    st.success("Volunteer Registration Successful")

st.markdown("---")

st.subheader("👥 Registered Volunteers")

cursor.execute("""
SELECT district, availability, contact_number, skills
FROM volunteers
ORDER BY id DESC
""")

volunteers = cursor.fetchall()

df = pd.DataFrame(
    volunteers,
    columns=[
        "District",
        "Availability",
        "Contact Number",
        "Skills"
    ]
)

st.dataframe(df, use_container_width=True)