"""
=========================================================
Dashboard
=========================================================
"""

import streamlit as st

def show_dashboard(df, model):

    st.title("📊 Employee Attrition Prediction & HR Analytics")

    st.markdown(
        """
Welcome to the Employee Attrition Prediction Dashboard.

This application predicts whether an employee is likely to leave the organization using Machine Learning.
"""
    )

    st.markdown("---")

    c1,c2,c3=st.columns(3)

    with c1:

        st.metric(
            "Employees",
            len(df)
        )

    with c2:

        st.metric(
            "Features",
            df.shape[1]-1
        )

    with c3:

        st.metric(
            "Model",
            type(model.named_steps["model"]).__name__
        )

    st.markdown("---")

    c1,c2,c3=st.columns(3)

    with c1:

        st.metric(
            "Attrition Rate",
            f"{((df['Attrition']=='Yes').mean()*100):.2f}%"
        )

    with c2:

        st.metric(
            "Average Age",
            f"{df['Age'].mean():.1f}"
        )

    with c3:

        st.metric(
            "Average Income",
            f"${df['MonthlyIncome'].mean():,.0f}"
        )

    st.markdown("---")