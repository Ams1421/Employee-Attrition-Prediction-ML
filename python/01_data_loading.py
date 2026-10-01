"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 2 : Data Loading
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Required Libraries
# -------------------------------------------------------

from config import RAW_DATASET
from utils import load_dataset, print_heading
from logger import logger

# -------------------------------------------------------
# Project Heading
# -------------------------------------------------------

print_heading("DATA LOADING")

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

try:

    df = load_dataset(RAW_DATASET)

    logger.info("Raw dataset loaded successfully.")

    print("Employee Attrition Dataset Loaded Successfully.")

except FileNotFoundError:

    logger.error("Dataset not found.")

    print(f"\nDataset not found:\n{RAW_DATASET}")

    exit()

except Exception as e:

    logger.exception("Unexpected error while loading dataset.")

    print(f"\nError: {e}")

    exit()

# -------------------------------------------------------
# Dataset Shape
# -------------------------------------------------------

print("\nDataset Shape")
print(df.shape)

# -------------------------------------------------------
# Column Names
# -------------------------------------------------------

print("\nColumns")
print(df.columns.tolist())

# -------------------------------------------------------
# First Five Records
# -------------------------------------------------------

print("\nFirst Five Rows")
print(df.head())

# -------------------------------------------------------
# Last Five Records
# -------------------------------------------------------

print("\nLast Five Rows")
print(df.tail())

# -------------------------------------------------------
# Data Types
# -------------------------------------------------------

print("\nData Types")
print(df.dtypes)

# -------------------------------------------------------
# Missing Values
# -------------------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# -------------------------------------------------------
# Duplicate Records
# -------------------------------------------------------

print("\nDuplicate Records")
print(df.duplicated().sum())

# -------------------------------------------------------
# Dataset Information
# -------------------------------------------------------

print("\nDataset Information")
df.info()

# -------------------------------------------------------
# Statistical Summary
# -------------------------------------------------------

print("\nStatistical Summary")
print(df.describe())

logger.info("Phase 2 - Data Loading completed successfully.")

print("\nPhase 2 Completed Successfully.")