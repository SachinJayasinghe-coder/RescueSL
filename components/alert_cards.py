import streamlit as st

def display_alert_card(
    disaster_type,
    district,
    severity
):

    if severity == "Critical":

        st.error(
            f"🚨 {disaster_type} detected in {district}"
        )

    elif severity == "High":

        st.warning(
            f"⚠️ {disaster_type} detected in {district}"
        )

    else:

        st.info(
            f"ℹ️ {disaster_type} detected in {district}"
        )