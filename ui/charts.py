"""
=========================================================
Employee Attrition Prediction
Charts
=========================================================
"""

import streamlit as st
import plotly.express as px


def show_charts(df):

    st.header("📊 HR Analytics Dashboard")

    col1, col2 = st.columns(2)

    # ---------------------------------------
    # Attrition Pie Chart
    # ---------------------------------------

    with col1:

        fig = px.pie(
            df,
            names="Attrition",
            title="Employee Attrition Distribution",
            hole=0.45
        )

        fig.update_layout(height=420)

        st.plotly_chart(
    fig,
    width="stretch"
)

    # ---------------------------------------
    # Department Chart
    # ---------------------------------------

    with col2:

        department_df = (
            df["Department"]
            .value_counts()
            .rename_axis("Department")
            .reset_index(name="Employees")
        )

        fig = px.bar(
            department_df,
            x="Department",
            y="Employees",
            title="Employees by Department",
            text="Employees"
        )

        fig.update_layout(height=420)

        st.plotly_chart(
    fig,
    width="stretch"
)

    st.markdown("---")

    # ---------------------------------------
    # Income Distribution
    # ---------------------------------------

    col3, col4 = st.columns(2)

    with col3:

        fig = px.histogram(
            df,
            x="MonthlyIncome",
            nbins=30,
            title="Monthly Income Distribution"
        )

        fig.update_layout(height=420)

        st.plotly_chart(
    fig,
    width="stretch"
)

    # ---------------------------------------
    # Age Distribution
    # ---------------------------------------

    with col4:

        fig = px.histogram(
            df,
            x="Age",
            nbins=20,
            title="Employee Age Distribution"
        )

        fig.update_layout(height=420)

        st.plotly_chart(
    fig,
    width="stretch"
)

    st.markdown("---")