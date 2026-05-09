import streamlit as st


def sidebar_navigation():

    st.sidebar.markdown(
        """
        <div style="
            text-align:center;
            padding-top:10px;
            padding-bottom:20px;
        ">

        <h1 style="
            color:#FF4B4B;
            font-size:36px;
            font-weight:800;
            margin-bottom:0px;
        ">
        🚨 Rescue SL
        </h1>

        <p style="
            color:white;
            font-size:14px;
            margin-top:5px;
        ">
        National Disaster Monitoring Platform
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("---")

    selected_page = st.sidebar.radio(

        "📌 Navigation Menu",

        [
            "Dashboard",
            "Report Disaster",
            "Live Map",
            "Live Alerts",
            "Verification Center",
            "Analytics",
            "Volunteer Center",
            "Emergency Contacts",
            "Admin Panel"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown(
        """
        <div style="
            background:rgba(255,255,255,0.05);
            padding:15px;
            border-radius:15px;
            border:1px solid rgba(255,255,255,0.08);
        ">

        <h3 style="
            color:#FF4B4B;
            margin-bottom:10px;
        ">
        🚨 System Status
        </h3>

        <p style="color:white;">
        ✔ Monitoring Active
        </p>

        <p style="color:white;">
        ✔ Emergency Alerts Enabled
        </p>

        <p style="color:white;">
        ✔ AI Verification Running
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        "Disaster Monitoring Services Online"
    )

    return selected_page