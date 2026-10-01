"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 10 : Business Insights
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Libraries
# -------------------------------------------------------

import pandas as pd

from config import CLEAN_DATASET, REPORT_DIR
from utils import load_dataset, save_report, print_heading
from logger import logger

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

df = load_dataset(CLEAN_DATASET)

print_heading("BUSINESS INSIGHTS")

logger.info("Business Insights Started")

# -------------------------------------------------------
# Overall Statistics
# -------------------------------------------------------

total_employees = len(df)

employees_left = (df["Attrition"] == "Yes").sum()

employees_stayed = (df["Attrition"] == "No").sum()

attrition_rate = (employees_left / total_employees) * 100

# -------------------------------------------------------
# Department-wise Attrition
# -------------------------------------------------------

department_attrition = (
    df[df["Attrition"] == "Yes"]
    .groupby("Department")
    .size()
    .sort_values(ascending=False)
)

# -------------------------------------------------------
# Job Role Attrition
# -------------------------------------------------------

jobrole_attrition = (
    df[df["Attrition"] == "Yes"]
    .groupby("JobRole")
    .size()
    .sort_values(ascending=False)
)

# -------------------------------------------------------
# Overtime Analysis
# -------------------------------------------------------

overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"]
)

# -------------------------------------------------------
# Average Monthly Income by Department
# -------------------------------------------------------

average_salary = (
    df.groupby("Department")["MonthlyIncome"]
    .mean()
    .round(2)
)

# -------------------------------------------------------
# Work-Life Balance Analysis
# -------------------------------------------------------

worklife = (
    df.groupby("WorkLifeBalance")["Attrition"]
    .value_counts()
)

# -------------------------------------------------------
# Display Results
# -------------------------------------------------------

print(f"\nTotal Employees      : {total_employees}")
print(f"Employees Stayed     : {employees_stayed}")
print(f"Employees Left       : {employees_left}")
print(f"Attrition Rate       : {attrition_rate:.2f}%")

print("\nDepartment-wise Attrition")
print(department_attrition)

print("\nTop Job Roles with Attrition")
print(jobrole_attrition.head())

print("\nOverTime vs Attrition")
print(overtime_attrition)

print("\nAverage Monthly Income by Department")
print(average_salary)

print("\nWork-Life Balance Analysis")
print(worklife)

# -------------------------------------------------------
# Create Report Content
# -------------------------------------------------------

report = f"""
EMPLOYEE ATTRITION BUSINESS INSIGHTS
======================================================================

Total Employees      : {total_employees}
Employees Stayed     : {employees_stayed}
Employees Left       : {employees_left}
Attrition Rate       : {attrition_rate:.2f}%

----------------------------------------------------------------------
Department-wise Attrition
----------------------------------------------------------------------

{department_attrition}

----------------------------------------------------------------------
Top Job Roles with Attrition
----------------------------------------------------------------------

{jobrole_attrition}

----------------------------------------------------------------------
OverTime Analysis
----------------------------------------------------------------------

{overtime_attrition}

----------------------------------------------------------------------
Average Monthly Income by Department
----------------------------------------------------------------------

{average_salary}

----------------------------------------------------------------------
Work-Life Balance Analysis
----------------------------------------------------------------------

{worklife}

======================================================================
HR RECOMMENDATIONS
======================================================================

1. Reduce excessive overtime where possible.

2. Improve employee engagement in high-attrition departments.

3. Focus retention strategies on high-risk job roles.

4. Strengthen work-life balance initiatives.

5. Review compensation and career growth opportunities.

6. Increase employee training and career development.

7. Conduct regular employee satisfaction surveys.

======================================================================
End of Report
======================================================================
"""

# -------------------------------------------------------
# Save Report
# -------------------------------------------------------

report_file = REPORT_DIR / "business_insights.txt"

save_report(report_file, report)

logger.info("Business Report Saved Successfully")

print("\nBusiness Report Saved Successfully")

print(report_file)

print("\nPhase 10 Completed Successfully.")

logger.info("Business Insights Completed")