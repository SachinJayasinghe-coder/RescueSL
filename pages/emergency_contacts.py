import streamlit as st
from styles import load_css

load_css()

st.title("☎️ Emergency Contact Center")

st.markdown("""
Quick access to national emergency service hotlines.
""")

st.markdown("---")

st.subheader("🚓 Police Emergency")

st.info("""
Emergency Hotline: 119
Sri Lanka Police Headquarters
""")

st.markdown("---")

st.subheader("🚑 Ambulance Service")

st.success("""
Suwa Seriya Ambulance Service: 1990
24/7 Emergency Medical Transport
""")

st.markdown("---")

st.subheader("🔥 Fire & Rescue")

st.error("""
Fire Brigade Emergency: 110
Disaster Fire Response Unit
""")

st.markdown("---")

st.subheader("🌊 Disaster Management Center")

st.warning("""
Disaster Management Center Hotline: 117
Floods, Landslides, Natural Disasters
""")

st.markdown("---")

st.subheader("🏥 Major Emergency Hospitals")

hospital_data = [
    {
        "Hospital": "National Hospital Colombo",
        "Contact": "0112691111"
    },
    {
        "Hospital": "Teaching Hospital Kandy",
        "Contact": "0812222261"
    },
    {
        "Hospital": "Karapitiya Teaching Hospital",
        "Contact": "0912232561"
    }
]

for hospital in hospital_data:

    st.markdown(f"""
    ### 🏥 {hospital['Hospital']}
    Contact Number: {hospital['Contact']}
    """)