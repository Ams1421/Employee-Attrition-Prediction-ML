"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 8 : Model Evaluation
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Libraries
# -------------------------------------------------------

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

from config import (
    CLEAN_DATASET,
    BEST_MODEL,
    LABEL_ENCODER,
    REPORT_DIR
)

from utils import (
    load_dataset,
    load_model,
    save_report,
    print_heading
)

from logger import logger

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

df = load_dataset(CLEAN_DATASET)

logger.info("Clean dataset loaded successfully.")

# -------------------------------------------------------
# Print Heading
# -------------------------------------------------------

print_heading("MODEL EVALUATION")

# -------------------------------------------------------
# Features & Target
# -------------------------------------------------------

X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# -------------------------------------------------------
# Load Saved Objects
# -------------------------------------------------------

label_encoder = load_model(LABEL_ENCODER)
best_model = load_model(BEST_MODEL)

logger.info("Best model and label encoder loaded.")

# -------------------------------------------------------
# Encode Target Variable
# -------------------------------------------------------

y = label_encoder.transform(y)

# -------------------------------------------------------
# Train-Test Split
# -------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -------------------------------------------------------
# Predictions
# -------------------------------------------------------

y_pred = best_model.predict(X_test)

logger.info("Prediction completed successfully.")

# -------------------------------------------------------
# Evaluation Metrics
# -------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred)

conf_matrix = confusion_matrix(y_test, y_pred)

report = classification_report(
    y_test,
    y_pred,
    target_names=label_encoder.classes_
)

# -------------------------------------------------------
# Display Results
# -------------------------------------------------------

print(f"\nAccuracy      : {accuracy:.4f}")
print(f"Precision     : {precision:.4f}")
print(f"Recall        : {recall:.4f}")
print(f"F1 Score      : {f1:.4f}")
print(f"ROC-AUC Score : {roc_auc:.4f}")

print("\nConfusion Matrix")
print(conf_matrix)

print("\nClassification Report")
print(report)

# -------------------------------------------------------
# Prepare Report
# -------------------------------------------------------

report_content = f"""
Employee Attrition Prediction
============================================================

Accuracy      : {accuracy:.4f}
Precision     : {precision:.4f}
Recall        : {recall:.4f}
F1 Score      : {f1:.4f}
ROC-AUC Score : {roc_auc:.4f}

Confusion Matrix
----------------
{conf_matrix}

Classification Report
---------------------
{report}
"""

# -------------------------------------------------------
# Save Report
# -------------------------------------------------------

report_file = REPORT_DIR / "model_metrics.txt"

save_report(report_file, report_content)

logger.info("Model evaluation report saved successfully.")

print("\nEvaluation Report Saved Successfully")
print(report_file)

print("\nPhase 8 Completed Successfully.")