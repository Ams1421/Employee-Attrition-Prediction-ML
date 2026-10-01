"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 5 : Data Visualization
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Libraries
# -------------------------------------------------------

import matplotlib.pyplot as plt

from config import CLEAN_DATASET, CHART_DIR
from utils import load_dataset, save_chart, print_heading
from logger import logger

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

df = load_dataset(CLEAN_DATASET)

print_heading("DATA VISUALIZATION")
logger.info("Clean dataset loaded successfully.")

# -------------------------------------------------------
# 1. Attrition Distribution
# -------------------------------------------------------

plt.figure(figsize=(6, 5))

df["Attrition"].value_counts().plot(
    kind="bar",
    color="steelblue"
)

plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Employee Count")
plt.grid(axis="y", alpha=0.3)

save_chart(CHART_DIR / "attrition_distribution.png")

logger.info("Attrition Distribution Chart Created")
print("✓ Attrition Distribution Created")

# -------------------------------------------------------
# 2. Department Distribution
# -------------------------------------------------------

plt.figure(figsize=(8, 5))

df["Department"].value_counts().plot(
    kind="bar",
    color="darkorange"
)

plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Employee Count")
plt.grid(axis="y", alpha=0.3)

save_chart(CHART_DIR / "department_distribution.png")

logger.info("Department Distribution Chart Created")
print("✓ Department Distribution Created")

# -------------------------------------------------------
# 3. Gender Distribution
# -------------------------------------------------------

plt.figure(figsize=(6, 6))

df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")
plt.ylabel("")

save_chart(CHART_DIR / "gender_distribution.png")

logger.info("Gender Distribution Chart Created")
print("✓ Gender Distribution Created")

# -------------------------------------------------------
# 4. Age Distribution
# -------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"],
    bins=15,
    edgecolor="black",
    color="skyblue"
)

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)

save_chart(CHART_DIR / "age_distribution.png")

logger.info("Age Distribution Chart Created")
print("✓ Age Distribution Created")

# -------------------------------------------------------
# 5. Monthly Income Distribution
# -------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["MonthlyIncome"],
    bins=20,
    edgecolor="black",
    color="green"
)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Employee Count")
plt.grid(alpha=0.3)

save_chart(CHART_DIR / "monthly_income_distribution.png")

logger.info("Monthly Income Distribution Chart Created")
print("✓ Monthly Income Distribution Created")

# -------------------------------------------------------
# 6. Overtime Distribution
# -------------------------------------------------------

plt.figure(figsize=(6, 5))

df["OverTime"].value_counts().plot(
    kind="bar",
    color="crimson"
)

plt.title("OverTime Distribution")
plt.xlabel("OverTime")
plt.ylabel("Employee Count")
plt.grid(axis="y", alpha=0.3)

save_chart(CHART_DIR / "overtime_distribution.png")

logger.info("OverTime Distribution Chart Created")
print("✓ OverTime Distribution Created")

# -------------------------------------------------------
# Summary
# -------------------------------------------------------

print("\n" + "=" * 70)
print("VISUALIZATION SUMMARY")
print("=" * 70)

print("Charts Generated : 6")
print(f"Charts Saved In : {CHART_DIR}")

logger.info("All visualization charts generated successfully.")

print("\nPhase 5 Completed Successfully.")