"""
=========================================================
Employee Attrition Prediction & HR Analytics
Project Configuration
=========================================================
"""

from pathlib import Path

# =========================================================
# PROJECT ROOT
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =========================================================
# DATASET PATHS
# =========================================================

DATASET_DIR = PROJECT_ROOT / "dataset"

RAW_DATASET = DATASET_DIR / "employee_attrition.csv"

CLEAN_DATASET = DATASET_DIR / "cleaned_employee_attrition.csv"

# =========================================================
# MODEL PATHS
# =========================================================

MODEL_DIR = PROJECT_ROOT / "models"

BEST_MODEL = MODEL_DIR / "best_model.pkl"

PREPROCESSOR = MODEL_DIR / "preprocessor.pkl"

LABEL_ENCODER = MODEL_DIR / "label_encoder.pkl"

# =========================================================
# OUTPUT PATHS
# =========================================================

OUTPUT_DIR = PROJECT_ROOT / "outputs"

REPORT_DIR = OUTPUT_DIR / "reports"

CHART_DIR = OUTPUT_DIR / "charts"

# =========================================================
# CREATE DIRECTORIES IF NOT EXIST
# =========================================================

MODEL_DIR.mkdir(parents=True, exist_ok=True)

REPORT_DIR.mkdir(parents=True, exist_ok=True)

CHART_DIR.mkdir(parents=True, exist_ok=True)