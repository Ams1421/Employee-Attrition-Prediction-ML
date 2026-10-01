"""
=========================================================
Sidebar
=========================================================
"""

import streamlit as st

def show_sidebar(df, model):

    st.sidebar.title("📊 HR Analytics")

    st.sidebar.success("Project Loaded Successfully")

    st.sidebar.markdown("---")

    st.sidebar.header("Dataset")

    st.sidebar.metric(
        "Employees",
        len(df)
    )

    st.sidebar.metric(
        "Features",
        df.shape[1]-1
    )

    st.sidebar.metric(
        "Target",
        "Attrition"
    )

    st.sidebar.markdown("---")

    st.sidebar.header("Machine Learning")

    st.sidebar.write(
        type(model.named_steps["model"]).__name__
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
### Employee Attrition Prediction

Built using

- Python

- Scikit-Learn

- Streamlit

- Plotly
"""
    )