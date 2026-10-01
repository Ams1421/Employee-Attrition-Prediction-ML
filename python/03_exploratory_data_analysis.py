"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 4 : Exploratory Data Analysis (EDA)
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Libraries
# -------------------------------------------------------

import pandas as pd

from config import CLEAN_DATASET, REPORT_DIR
from utils import load_dataset, print_heading
from logger import logger

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

df = load_dataset(CLEAN_DATASET)

print_heading("EXPLORATORY DATA ANALYSIS")

logger.info("Clean dataset loaded successfully.")

# -------------------------------------------------------
# Dataset Information
# -------------------------------------------------------

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns.tolist())

# -------------------------------------------------------
# Numerical Summary
# -------------------------------------------------------

print("\nNumerical Summary")
print(df.describe())

# -------------------------------------------------------
# Categorical Summary
# -------------------------------------------------------

print("\nCategorical Summary")
print(df.describe(include="string"))

# -------------------------------------------------------
# Attrition Distribution
# -------------------------------------------------------

print("\nEmployee Attrition Count")
print(df["Attrition"].value_counts())

print("\nEmployee Attrition Percentage")
print(round(df["Attrition"].value_counts(normalize=True) * 100, 2))

# -------------------------------------------------------
# Department Analysis
# -------------------------------------------------------

print("\nDepartment Distribution")
print(df["Department"].value_counts())

# -------------------------------------------------------
# Gender Distribution
# -------------------------------------------------------

print("\nGender Distribution")
print(df["Gender"].value_counts())

# -------------------------------------------------------
# Job Role Distribution
# -------------------------------------------------------

print("\nJob Role Distribution")
print(df["JobRole"].value_counts())

# -------------------------------------------------------
# Overtime Analysis
# -------------------------------------------------------

print("\nOverTime Distribution")
print(df["OverTime"].value_counts())

# -------------------------------------------------------
# Education Distribution
# -------------------------------------------------------

print("\nEducation Levels")
print(df["Education"].value_counts().sort_index())

# -------------------------------------------------------
# Marital Status
# -------------------------------------------------------

print("\nMarital Status")
print(df["MaritalStatus"].value_counts())

# -------------------------------------------------------
# Average Monthly Income
# -------------------------------------------------------

print("\nAverage Monthly Income")
print(f"${df['MonthlyIncome'].mean():,.2f}")

# -------------------------------------------------------
# Average Age
# -------------------------------------------------------

print("\nAverage Employee Age")
print(round(df["Age"].mean(), 2))

# -------------------------------------------------------
# Correlation Matrix
# -------------------------------------------------------

print("\nCorrelation Matrix")

correlation = df.select_dtypes(include="number").corr()

print(correlation)

# -------------------------------------------------------
# Save Correlation Matrix
# -------------------------------------------------------

correlation.to_csv(REPORT_DIR / "correlation_matrix.csv")

logger.info("Correlation matrix saved successfully.")

print("\nCorrelation Matrix Saved Successfully")

logger.info("Exploratory Data Analysis completed successfully.")

print("\nEDA Completed Successfully.")