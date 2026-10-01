"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 3 : Data Cleaning
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Libraries
# -------------------------------------------------------

import pandas as pd

from config import RAW_DATASET, CLEAN_DATASET

from utils import (
    load_dataset,
    save_dataset,
    print_heading
)

from logger import logger

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

try:
    df = load_dataset(RAW_DATASET)
    logger.info("Raw dataset loaded successfully.")

except Exception as e:
    logger.error(f"Failed to load dataset: {e}")
    raise

print_heading("DATA CLEANING")

# -------------------------------------------------------
# Dataset Shape
# -------------------------------------------------------

print(f"\nOriginal Shape : {df.shape}")

# -------------------------------------------------------
# Missing Values
# -------------------------------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# -------------------------------------------------------
# Duplicate Records
# -------------------------------------------------------

duplicates = df.duplicated().sum()

print(f"\nDuplicate Records : {duplicates}")

# -------------------------------------------------------
# Constant Columns
# -------------------------------------------------------

print("\nConstant Columns")

constant_columns = []

for column in df.columns:

    if df[column].nunique() == 1:

        constant_columns.append(column)

print(constant_columns)

# -------------------------------------------------------
# Remove Constant Columns
# -------------------------------------------------------

df.drop(columns=constant_columns, inplace=True)

print(f"\nShape After Removing Constant Columns : {df.shape}")

# -------------------------------------------------------
# Unique Values
# -------------------------------------------------------

print("\nUnique Values Per Column")

for column in df.columns:

    print(f"{column:<30} : {df[column].nunique()}")

# -------------------------------------------------------
# Target Variable Distribution
# -------------------------------------------------------

print("\nTarget Variable Distribution")

print(df["Attrition"].value_counts())

print("\nTarget Variable Percentage")

print(round(df["Attrition"].value_counts(normalize=True) * 100, 2))

# -------------------------------------------------------
# Save Clean Dataset
# -------------------------------------------------------

save_dataset(df, CLEAN_DATASET)

logger.info("Clean dataset saved successfully.")

# -------------------------------------------------------
# Completion Message
# -------------------------------------------------------

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 70)

logger.info("Data cleaning completed successfully.")