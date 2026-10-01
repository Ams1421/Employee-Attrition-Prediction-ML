"""
=========================================================
Employee Input Form
=========================================================
"""

import streamlit as st

def employee_form():

    with st.form("employee_form"):

        st.header("👤 Employee Information")

        # =======================================
        # Personal Information
        # =======================================

        st.subheader("👤 Personal Information")

        col1, col2 = st.columns(2)

        with col1:

            age = st.slider("Age",18,60,35)

            gender = st.selectbox(
                "Gender",
                ["Male","Female"]
            )

            marital_status = st.selectbox(
                "Marital Status",
                [
                    "Single",
                    "Married",
                    "Divorced"
                ]
            )

            education = st.selectbox(
                "Education",
                [1,2,3,4,5]
            )

        with col2:

            education_field = st.selectbox(
                "Education Field",
                [
                    "Life Sciences",
                    "Medical",
                    "Marketing",
                    "Technical Degree",
                    "Human Resources",
                    "Other"
                ]
            )

            distance = st.slider(
                "Distance From Home",
                1,
                30,
                5
            )

            business_travel = st.selectbox(
                "Business Travel",
                [
                    "Travel_Rarely",
                    "Travel_Frequently",
                    "Non-Travel"
                ]
            )

        # =======================================
        # Job Information
        # =======================================

        st.subheader("💼 Job Information")

        col3, col4 = st.columns(2)

        with col3:

            department = st.selectbox(
                "Department",
                [
                    "Research & Development",
                    "Sales",
                    "Human Resources"
                ]
            )

            job_role = st.selectbox(
                "Job Role",
                [
                    "Sales Executive",
                    "Research Scientist",
                    "Laboratory Technician",
                    "Manufacturing Director",
                    "Healthcare Representative",
                    "Manager",
                    "Sales Representative",
                    "Research Director",
                    "Human Resources"
                ]
            )

            job_level = st.slider("Job Level",1,5,2)

            job_involvement = st.slider(
                "Job Involvement",
                1,
                4,
                3
            )

        with col4:

            environment = st.slider(
                "Environment Satisfaction",
                1,
                4,
                3
            )

            job_satisfaction = st.slider(
                "Job Satisfaction",
                1,
                4,
                3
            )

            relationship = st.slider(
                "Relationship Satisfaction",
                1,
                4,
                3
            )

            overtime = st.selectbox(
                "OverTime",
                ["No","Yes"]
            )

        # =======================================
        # Salary
        # =======================================

        st.subheader("💰 Salary Information")

        col5,col6=st.columns(2)

        with col5:

            daily_rate = st.number_input(
                "Daily Rate",
                100,
                1500,
                800
            )

            hourly_rate = st.number_input(
                "Hourly Rate",
                30,
                100,
                70
            )

            monthly_income = st.number_input(
                "Monthly Income",
                1000,
                25000,
                6500
            )

        with col6:

            monthly_rate = st.number_input(
                "Monthly Rate",
                2000,
                30000,
                12000
            )

            salary_hike = st.slider(
                "Percent Salary Hike",
                10,
                25,
                15
            )

            stock_option = st.slider(
                "Stock Option Level",
                0,
                3,
                1
            )

        # =======================================
        # Experience
        # =======================================

        st.subheader("🏢 Experience")

        col7,col8=st.columns(2)

        with col7:

            total_years = st.slider(
                "Total Working Years",
                0,
                40,
                10
            )

            years_company = st.slider(
                "Years At Company",
                0,
                40,
                8
            )

            years_role = st.slider(
                "Years In Current Role",
                0,
                20,
                5
            )

        with col8:

            years_manager = st.slider(
                "Years With Current Manager",
                0,
                20,
                5
            )

            years_promotion = st.slider(
                "Years Since Last Promotion",
                0,
                15,
                1
            )

            training = st.slider(
                "Training Times Last Year",
                0,
                10,
                3
            )

        # =======================================
        # Work Environment
        # =======================================

        st.subheader("😊 Work Environment")

        col9,col10=st.columns(2)

        with col9:

            worklife = st.slider(
                "Work Life Balance",
                1,
                4,
                3
            )

            performance = st.selectbox(
                "Performance Rating",
                [3,4]
            )

        with col10:

            companies = st.slider(
                "Number of Companies Worked",
                0,
                10,
                2
            )

        submitted = st.form_submit_button(
            "🔮 Predict Attrition",
            width="stretch"
        )

    return submitted, {
        "Age": age,
        "BusinessTravel": business_travel,
        "DailyRate": daily_rate,
        "Department": department,
        "DistanceFromHome": distance,
        "Education": education,
        "EducationField": education_field,
        "EmployeeNumber": 9999,
        "EnvironmentSatisfaction": environment,
        "Gender": gender,
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobRole": job_role,
        "JobSatisfaction": job_satisfaction,
        "MaritalStatus": marital_status,
        "MonthlyIncome": monthly_income,
        "MonthlyRate": monthly_rate,
        "NumCompaniesWorked": companies,
        "OverTime": overtime,
        "PercentSalaryHike": salary_hike,
        "PerformanceRating": performance,
        "RelationshipSatisfaction": relationship,
        "StockOptionLevel": stock_option,
        "TotalWorkingYears": total_years,
        "TrainingTimesLastYear": training,
        "WorkLifeBalance": worklife,
        "YearsAtCompany": years_company,
        "YearsInCurrentRole": years_role,
        "YearsSinceLastPromotion": years_promotion,
        "YearsWithCurrManager": years_manager
    }