import streamlit as st

from database import cursor
from database import connection

from styles import load_css

load_css()

st.title("✅ Verification Center")

st.markdown("---")

cursor.execute(
    """
    SELECT

        id,
        disaster_type,
        district,
        verification_count,
        severity

    FROM reports

    ORDER BY id DESC
"""
)

reports = cursor.fetchall()

for report in reports:

    report_id = report[0]

    disaster_type = report[1]

    district = report[2]

    verification_count = report[3]

    severity = report[4]

    st.subheader(
        f"{disaster_type} - {district}"
    )

    st.write(
        f"Verification Count: {verification_count}"
    )

    st.write(
        f"Severity Level: {severity}"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            f"Confirm Report {report_id}"
        ):

            updated_count = verification_count + 1

            cursor.execute(
                """
                UPDATE reports

                SET verification_count=?

                WHERE id=?
                """,

                (
                    updated_count,
                    report_id
                )
            )

            connection.commit()

            st.success(
                "Report Confirmed Successfully"
            )

    with col2:

        if st.button(
            f"Mark As Suspicious {report_id}"
        ):

            st.error(
                "Report Flagged For Further Review"
            )

    st.markdown("---")