import streamlit as st
import pandas as pd
from database import cursor, connection
from styles import load_css

load_css()

st.title("🛠️ Rescue SL Admin Dashboard")

st.markdown("""
Administrative monitoring and disaster management center.
""")

st.markdown("---")

cursor.execute("SELECT COUNT(*) FROM users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM reports")
total_reports = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM volunteers")
total_volunteers = cursor.fetchone()[0]

cursor.execute("""
SELECT COUNT(*)
FROM reports
WHERE severity='Critical'
""")

critical_reports = cursor.fetchone()[0]

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="glass-card">

    <h3 style="color:#D6E4FF;">
    Users
    </h3>

    <h1 style="color:white;font-size:48px;">
    {total_users}
    </h1>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="glass-card">

    <h3 style="color:#D6E4FF;">
    Reports
    </h3>

    <h1 style="color:white;font-size:48px;">
    {total_reports}
    </h1>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="glass-card">

    <h3 style="color:#D6E4FF;">
    Volunteers
    </h3>

    <h1 style="color:white;font-size:48px;">
    {total_volunteers}
    </h1>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="glass-card">

    <h3 style="color:#D6E4FF;">
    Critical Alerts
    </h3>

    <h1 style="color:white;font-size:48px;">
    {critical_reports}
    </h1>

    </div>
    """, unsafe_allow_html=True)

st.subheader("📋 Manage Disaster Reports")

cursor.execute("""
SELECT
    id,
    disaster_type,
    district,
    severity,
    verification_count,
    status,
    created_at
FROM reports
ORDER BY id DESC
""")

reports = cursor.fetchall()

df = pd.DataFrame(
    reports,
    columns=[
        "ID",
        "Disaster Type",
        "District",
        "Severity",
        "Verification Count",
        "Status",
        "Created At"
    ]
)

st.dataframe(df, use_container_width=True)

st.markdown("---")

st.subheader("🗑️ Delete Fake Reports")

report_id = st.number_input(
    "Enter Report ID",
    min_value=1,
    step=1
)

if st.button("Delete Report"):

    cursor.execute(
        "DELETE FROM reports WHERE id=?",
        (report_id,)
    )

    connection.commit()

    st.success("Report Deleted Successfully")

st.markdown("---")

st.subheader("🚨 Emergency Monitoring Feed")

cursor.execute("""
SELECT disaster_type, district, severity
FROM reports
ORDER BY id DESC
LIMIT 10
""")

feed = cursor.fetchall()

for item in feed:

    disaster_type = item[0]
    district = item[1]
    severity = item[2]

    if severity == "Critical":

        st.error(
            f"🚨 CRITICAL: {disaster_type} detected in {district}"
        )

    elif severity == "High":

        st.warning(
            f"⚠️ HIGH RISK: {disaster_type} detected in {district}"
        )

    else:

        st.info(
            f"ℹ️ {disaster_type} reported in {district}"
        )