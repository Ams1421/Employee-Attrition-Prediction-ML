"""
=========================================================
Prediction Module
=========================================================
"""

import pandas as pd
import streamlit as st

def predict_employee(model, encoder, employee):

    employee_df = pd.DataFrame([employee])

    with st.spinner("Predicting Employee Attrition..."):

        prediction = model.predict(employee_df)[0]

        probability = model.predict_proba(employee_df)[0]

    prediction_label = encoder.inverse_transform([prediction])[0]

    stay_probability = probability[0] * 100
    leave_probability = probability[1] * 100

    confidence = max(
        stay_probability,
        leave_probability
    )

    return (
        prediction_label,
        stay_probability,
        leave_probability,
        confidence
    )


def show_prediction(
    prediction_label,
    stay_probability,
    leave_probability,
    confidence
):

    st.markdown("---")

    container = st.container(border=True)

    with container:

        st.header("Prediction Result")

        if prediction_label == "No":

            st.success(
                "✅ Employee is likely to Stay"
            )

            st.balloons()

        else:

            st.error(
                "⚠️ Employee is likely to Leave"
            )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Prediction",
                "Stay"
                if prediction_label == "No"
                else "Leave"
            )

        with col2:

            st.metric(
                "Stay Probability",
                f"{stay_probability:.2f}%"
            )

        with col3:

            st.metric(
                "Leave Probability",
                f"{leave_probability:.2f}%"
            )

        st.progress(confidence / 100)

        st.info(
            f"Model Confidence : {confidence:.2f}%"
        )