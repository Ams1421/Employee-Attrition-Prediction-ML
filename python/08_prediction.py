"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 9 : Prediction System
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Libraries
# -------------------------------------------------------

import pandas as pd

from config import BEST_MODEL, LABEL_ENCODER
from utils import load_model, print_heading
from logger import logger

# -------------------------------------------------------
# Heading
# -------------------------------------------------------

print_heading("EMPLOYEE ATTRITION PREDICTION")

# -------------------------------------------------------
# Load Saved Model
# -------------------------------------------------------

try:
    model = load_model(BEST_MODEL)
    label_encoder = load_model(LABEL_ENCODER)

    logger.info("Best model loaded successfully.")
    logger.info("Label encoder loaded successfully.")

except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise

# -------------------------------------------------------
# Sample Employee Data
# -------------------------------------------------------

employee = {
    "Age": 35,
    "BusinessTravel": "Travel_Rarely",
    "DailyRate": 800,
    "Department": "Research & Development",
    "DistanceFromHome": 5,
    "Education": 3,
    "EducationField": "Life Sciences",
    "EmployeeNumber": 2001,
    "EnvironmentSatisfaction": 3,
    "Gender": "Male",
    "HourlyRate": 70,
    "JobInvolvement": 3,
    "JobLevel": 2,
    "JobRole": "Research Scientist",
    "JobSatisfaction": 4,
    "MaritalStatus": "Married",
    "MonthlyIncome": 6500,
    "MonthlyRate": 12000,
    "NumCompaniesWorked": 2,
    "OverTime": "No",
    "PercentSalaryHike": 15,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 3,
    "StockOptionLevel": 1,
    "TotalWorkingYears": 10,
    "TrainingTimesLastYear": 3,
    "WorkLifeBalance": 3,
    "YearsAtCompany": 8,
    "YearsInCurrentRole": 5,
    "YearsSinceLastPromotion": 1,
    "YearsWithCurrManager": 5
}

# -------------------------------------------------------
# Convert to DataFrame
# -------------------------------------------------------

employee_df = pd.DataFrame([employee])

logger.info("Employee data prepared for prediction.")

# -------------------------------------------------------
# Prediction
# -------------------------------------------------------

prediction = model.predict(employee_df)[0]

prediction_label = label_encoder.inverse_transform([prediction])[0]

logger.info(f"Prediction completed: {prediction_label}")

# -------------------------------------------------------
# Prediction Probability
# -------------------------------------------------------

probability = model.predict_proba(employee_df)[0]

stay_probability = probability[0] * 100
leave_probability = probability[1] * 100

# -------------------------------------------------------
# Display Result
# -------------------------------------------------------

print("\nPrediction Result")
print("-" * 40)

print(f"Prediction               : {prediction_label}")
print(f"Probability of Staying   : {stay_probability:.2f}%")
print(f"Probability of Leaving   : {leave_probability:.2f}%")

print("\nPrediction Completed Successfully.")

logger.info("Prediction system executed successfully.")