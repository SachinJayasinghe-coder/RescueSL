import streamlit as st

from database import cursor

from styles import load_css

load_css()

st.title("📢 Live Emergency Alerts")

st.markdown("---")

cursor.execute(
    """
    SELECT

        disaster_type,
        district,
        severity,
        created_at

    FROM reports

    ORDER BY id DESC

    LIMIT 20
"""
)

alerts = cursor.fetchall()

for alert in alerts:

    disaster_type = alert[0]

    district = alert[1]

    severity = alert[2]

    created_at = alert[3]

    if severity == "Critical":

        st.error(
            f"🚨 {disaster_type} reported in {district} | Severity: {severity}"
        )

    elif severity == "High":

        st.warning(
            f"⚠️ {disaster_type} reported in {district} | Severity: {severity}"
        )

    else:

        st.info(
            f"ℹ️ {disaster_type} reported in {district} | Severity: {severity}"
        )

    st.caption(created_at)

    st.markdown("---")