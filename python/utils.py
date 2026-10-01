"""
=========================================================
Employee Attrition Prediction & HR Analytics
Utility Functions
=========================================================
"""

import joblib
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# DATASET FUNCTIONS
# ---------------------------------------------------------

def load_dataset(path):
    """
    Load CSV dataset.
    """
    return pd.read_csv(path)


def save_dataset(df, path):
    """
    Save dataframe as CSV.
    """
    df.to_csv(path, index=False)


# ---------------------------------------------------------
# MODEL FUNCTIONS
# ---------------------------------------------------------

def save_model(model, path):
    """
    Save ML model.
    """
    joblib.dump(model, path)


def load_model(path):
    """
    Load ML model.
    """
    return joblib.load(path)


# ---------------------------------------------------------
# REPORT FUNCTION
# ---------------------------------------------------------

def save_report(path, content):
    """
    Save text report.
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


# ---------------------------------------------------------
# CHART FUNCTION
# ---------------------------------------------------------

def save_chart(path):
    """
    Save matplotlib chart.
    """
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------
# PRINT HEADING
# ---------------------------------------------------------

def print_heading(title):
    """
    Print formatted heading.
    """
    print("=" * 70)
    print(title)
    print("=" * 70)