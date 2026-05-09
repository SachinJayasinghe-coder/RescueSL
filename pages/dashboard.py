import streamlit as st
import pandas as pd

from database import cursor

from styles import load_css

load_css()

# HERO SECTION

st.markdown("""
<div style="
background: linear-gradient(
135deg,
rgba(255,75,75,0.18),
rgba(255,107,107,0.08)
);
padding:35px;
border-radius:28px;
border:1px solid rgba(255,255,255,0.08);
margin-bottom:25px;
box-shadow:0px 8px 32px rgba(0,0,0,0.35);
backdrop-filter: blur(12px);
text-align:center;
">

<h1 style="
color:white;
font-size:64px;
font-weight:900;
margin-bottom:10px;
letter-spacing:2px;
">
🚨 Rescue SL
</h1>

<p style="
color:#D6E4FF;
font-size:20px;
margin-bottom:0px;
">
AI-Powered National Disaster Monitoring Platform
</p>

</div>
""", unsafe_allow_html=True)

st.title("🏠 Dashboard")

st.markdown("---")

# DATABASE COUNTS

cursor.execute(
    "SELECT COUNT(*) FROM reports"
)

total_reports = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM users"
)

total_users = cursor.fetchone()[0]

cursor.execute(
    """
    SELECT COUNT(*)
    FROM reports
    WHERE disaster_type='Flood'
    """
)

flood_reports = cursor.fetchone()[0]

cursor.execute(
    """
    SELECT COUNT(*)
    FROM reports
    WHERE disaster_type='Fire'
    """
)

fire_reports = cursor.fetchone()[0]

# DASHBOARD CARDS

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="glass-card">

    <h3 style="
        color:#D6E4FF;
        font-size:20px;
    ">
    Total Reports
    </h3>

    <h1 style="
        color:white;
        font-size:52px;
        font-weight:900;
    ">
    {total_reports}
    </h1>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="glass-card">

    <h3 style="
        color:#D6E4FF;
        font-size:20px;
    ">
    Total Users
    </h3>

    <h1 style="
        color:white;
        font-size:52px;
        font-weight:900;
    ">
    {total_users}
    </h1>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="glass-card">

    <h3 style="
        color:#D6E4FF;
        font-size:20px;
    ">
    Flood Reports
    </h3>

    <h1 style="
        color:white;
        font-size:52px;
        font-weight:900;
    ">
    {flood_reports}
    </h1>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="glass-card">

    <h3 style="
        color:#D6E4FF;
        font-size:20px;
    ">
    Fire Reports
    </h3>

    <h1 style="
        color:white;
        font-size:52px;
        font-weight:900;
    ">
    {fire_reports}
    </h1>

    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# RECENT REPORTS

st.subheader("🚨 Recent Disaster Reports")

cursor.execute(
    """
    SELECT

        disaster_type,
        district,
        severity,
        verification_count,
        created_at

    FROM reports

    ORDER BY id DESC

    LIMIT 10
    """
)

reports = cursor.fetchall()

dataframe = pd.DataFrame(

    reports,

    columns=[
        "Disaster Type",
        "District",
        "Severity",
        "Verification Count",
        "Created At"
    ]
)

st.dataframe(
    dataframe,
    use_container_width=True
)

st.markdown("---")

# ALERT CENTER

st.subheader("📢 Emergency Warning Center")

st.error(
    "Heavy rainfall warning issued for Western Province."
)

st.warning(
    "Possible landslide risks in Kandy district."
)

st.success(
    "Emergency response teams active in Colombo."
)
st.markdown("---")

st.markdown("""
<div style="
text-align:center;
padding:20px;
color:#B8C7E0;
font-size:16px;
">

Developed By 
<span style="
color:#FF4B4B;
font-weight:700;
">
@Sachin Jayasinghe
</span><br>
📅 2026
</div>
""", unsafe_allow_html=True)