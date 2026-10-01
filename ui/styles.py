"""
=========================================================
Employee Attrition Prediction
Custom Streamlit Styles
=========================================================
"""

import streamlit as st

def load_css():

    st.markdown(
        """
<style>

/* -----------------------------
Main Page
------------------------------*/

.main{

    background-color:#f8fafc;

}

/* -----------------------------
Title
------------------------------*/

h1{

    color:#0f172a;

    text-align:center;

    font-weight:bold;

}

/* -----------------------------
Headers
------------------------------*/

h2,h3{

    color:#2563eb;

}

/* -----------------------------
Metric Cards
------------------------------*/

[data-testid="metric-container"]{

    background:white;

    border-radius:15px;

    padding:18px;

    box-shadow:0px 2px 12px rgba(0,0,0,.08);

}

/* -----------------------------
Sidebar
------------------------------*/

section[data-testid="stSidebar"]{

    background:#eff6ff;

}

/* -----------------------------
Buttons
------------------------------*/

div.stButton > button{

    width:100%;

    height:55px;

    font-size:18px;

    border-radius:12px;

    font-weight:bold;

}

/* -----------------------------
Footer
------------------------------*/

footer{

    visibility:hidden;

}

</style>
        """,
        unsafe_allow_html=True
    )