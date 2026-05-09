import streamlit as st

from styles import load_css

from components.sidebar import sidebar_navigation

st.set_page_config(
    page_title="Rescue SL",
    page_icon="🚨",
    layout="wide"
)

load_css()

selected_page = sidebar_navigation()

if selected_page == "Dashboard":

    exec(
        open(
            "pages/dashboard.py",
            encoding="utf-8"
        ).read()
    )

elif selected_page == "Report Disaster":

    exec(
        open(
            "pages/report_disaster.py",
            encoding="utf-8"
        ).read()
    )

elif selected_page == "Live Map":

    exec(
        open(
            "pages/live_map.py",
            encoding="utf-8"
        ).read()
    )

elif selected_page == "Live Alerts":

    exec(
        open(
            "pages/live_alerts.py",
            encoding="utf-8"
        ).read()
    )

elif selected_page == "Verification Center":

    exec(
        open(
            "pages/verification_center.py",
            encoding="utf-8"
        ).read()
    )

elif selected_page == "Analytics":

    exec(
        open(
            "pages/analytics.py",
            encoding="utf-8"
        ).read()
    )

elif selected_page == "Volunteer Center":

    exec(
        open(
            "pages/volunteer_center.py",
            encoding="utf-8"
        ).read()
    )

elif selected_page == "Emergency Contacts":

    exec(
        open(
            "pages/emergency_contacts.py",
            encoding="utf-8"
        ).read()
    )

elif selected_page == "Admin Panel":

    exec(
        open(
            "pages/admin_panel.py",
            encoding="utf-8"
        ).read()
    )