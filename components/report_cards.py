import streamlit as st

def display_report_card(
    disaster_type,
    district,
    severity,
    verification_count,
    ai_confidence
):

    st.markdown(
        f"""
        <div style='
            background:rgba(255,255,255,0.05);
            padding:20px;
            border-radius:15px;
            margin-bottom:15px;
            border:1px solid rgba(255,255,255,0.08);
        '>

        <h3 style='color:#FF4B4B;'>
        🚨 {disaster_type}
        </h3>

        <p style='color:white;'>
        <strong>District:</strong> {district}
        </p>

        <p style='color:white;'>
        <strong>Severity:</strong> {severity}
        </p>

        <p style='color:white;'>
        <strong>Verification Count:</strong> {verification_count}
        </p>

        <p style='color:white;'>
        <strong>AI Confidence:</strong> {ai_confidence}%
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )