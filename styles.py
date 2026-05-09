import streamlit as st

def load_css():

    st.markdown(
        """
        <style>

        /* MAIN BACKGROUND */

        .stApp {

            background:
            linear-gradient(
                135deg,
                #071330 0%,
                #0B1020 35%,
                #10192D 100%
            );

            color: white;
        }

        footer {
            visibility: hidden;
        }

        /* SIDEBAR */

        section[data-testid="stSidebar"] {

            background:
            linear-gradient(
                180deg,
                #0B1020 0%,
                #071330 100%
            );

            border-right:
            1px solid rgba(255,255,255,0.08);
        }

        /* SIDEBAR TEXT */

        section[data-testid="stSidebar"] * {

            color: white !important;
        }

        /* SIDEBAR TITLES */

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {

            color: #FF4B4B !important;
        }

        /* RADIO LABELS */

        .stRadio label {

            color: white !important;

            font-size: 16px !important;

            font-weight: 500 !important;
        }

        /* MAIN TITLE */

        .main-title {

            font-size: 52px;

            font-weight: 800;

            color: #FF4B4B;

            text-align: center;

            margin-top: 10px;

            margin-bottom: 20px;

            text-shadow:
            0px 0px 20px rgba(255,75,75,0.4);
        }

        /* HEADINGS */

        h1, h2, h3 {

            color: white !important;
        }

        /* GLASS CARD */

        .glass-card {

            background:
            rgba(255,255,255,0.05);

            backdrop-filter: blur(14px);

            border:
            1px solid rgba(255,255,255,0.08);

            border-radius: 22px;

            padding: 25px;

            margin-bottom: 20px;

            box-shadow:
            0px 8px 32px rgba(0,0,0,0.35);

            transition: 0.3s;
        }

        .glass-card:hover {

            transform: translateY(-3px);

            box-shadow:
            0px 10px 40px rgba(0,0,0,0.45);
        }

        /* ALERT BOXES */

        .critical-alert {

            background:
            rgba(255,75,75,0.12);

            border-left:
            6px solid #FF4B4B;

            padding: 18px;

            border-radius: 14px;

            margin-bottom: 15px;

            box-shadow:
            0px 0px 18px rgba(255,75,75,0.2);
        }

        .warning-alert {

            background:
            rgba(255,159,28,0.12);

            border-left:
            6px solid #FF9F1C;

            padding: 18px;

            border-radius: 14px;

            margin-bottom: 15px;
        }

        .safe-alert {

            background:
            rgba(46,196,182,0.12);

            border-left:
            6px solid #2EC4B6;

            padding: 18px;

            border-radius: 14px;

            margin-bottom: 15px;
        }

        /* METRIC CARDS */

        div[data-testid="metric-container"] {

            background:
            rgba(255,255,255,0.08);

            border:
            1px solid rgba(255,255,255,0.08);

            padding: 20px;

            border-radius: 20px;

            box-shadow:
            0px 4px 20px rgba(0,0,0,0.25);
        }

        /* METRIC LABELS */

        div[data-testid="metric-container"] label {

            color:  !important;

            font-size: 17px !important;

            font-weight: 700 !important;
        }

        /* METRIC VALUES */

        div[data-testid="stMetricValue"] {

            color: white !important;

            font-size: 42px !important;

            font-weight: 800 !important;
        }

        /* BUTTONS */

        .stButton > button {

            width: 100%;

            border-radius: 14px;

            border: none;

            background:
            linear-gradient(
                90deg,
                #FF4B4B,
                #FF6B6B
            );

            color: white;

            font-size: 16px;

            font-weight: 600;

            padding: 12px;

            transition: 0.3s;
        }

        .stButton > button:hover {

            transform: scale(1.02);

            box-shadow:
            0px 0px 18px rgba(255,75,75,0.4);
        }

        /* INPUT FIELDS */

        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div,
        .stNumberInput input {

            border-radius: 12px !important;

            background:
            rgba(255,255,255,0.05) !important;

            color: white !important;

            border:
            1px solid rgba(255,255,255,0.08) !important;
        }

        /* DATAFRAMES */

        .stDataFrame {

            border-radius: 18px;

            overflow: hidden;
        }

        /* ALERTS */

        .stAlert {

            border-radius: 14px !important;
        }

        /* SCROLLBAR */

        ::-webkit-scrollbar {

            width: 10px;
        }

        ::-webkit-scrollbar-thumb {

            background: #FF4B4B;

            border-radius: 10px;
        }

        /* MAP */

        iframe {

            border-radius: 20px !important;

            border:
            1px solid rgba(255,255,255,0.08) !important;
        }

        /* FORM LABELS */

        label,
        .stTextInput label,
        .stTextArea label,
        .stSelectbox label,
        .stNumberInput label,
        .stFileUploader label {

            color: white !important;

            font-size: 18px !important;

            font-weight: 600 !important;
        }

        /* SELECTBOX TEXT */

        .stSelectbox div[data-baseweb="select"] {

            color: white !important;
        }

        /* INPUT TEXT */

        input,
        textarea {

            color: white !important;

            caret-color: white !important;
        }

        /* TEXT AREA FIX */

        .stTextArea textarea {

            background-color:
            rgba(20,25,45,0.95) !important;

            color: white !important;

            border:
            1px solid rgba(255,255,255,0.12) !important;
        }
                /* NUMBER INPUT FIX */

        .stNumberInput input {

            background-color:
            rgba(20,25,45,0.95) !important;

            color: white !important;

            caret-color: white !important;

            border:
            1px solid rgba(255,255,255,0.12) !important;
        }

        section[data-testid="stSidebarNa"] {
            display:none
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )