import streamlit as st

def display_navbar():

    st.markdown(
        """
        <div style='
            background-color:#0B1020;
            padding:15px;
            border-radius:10px;
            margin-bottom:20px;
            border:1px solid rgba(255,255,255,0.1);
        '>

        <h2 style='
            color:white;
            text-align:center;
        '>
        🚨 Rescue SL National Disaster Monitoring Platform
        </h2>

        </div>
        """,
        unsafe_allow_html=True
    )