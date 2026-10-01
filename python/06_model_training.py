"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 7 : Model Training
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Libraries
# -------------------------------------------------------

import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from sklearn.metrics import accuracy_score

# -------------------------------------------------------
# Import Project Modules
# -------------------------------------------------------

from config import (
    CLEAN_DATASET,
    PREPROCESSOR,
    LABEL_ENCODER,
    BEST_MODEL
)

from utils import (
    load_dataset,
    load_model,
    save_model,
    print_heading
)

from logger import logger

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

df = load_dataset(CLEAN_DATASET)

print_heading("MODEL TRAINING")
logger.info("Clean dataset loaded successfully.")

# -------------------------------------------------------
# Features & Target
# -------------------------------------------------------

X = df.drop("Attrition", axis=1)
y = df["Attrition"]

logger.info("Features and target variable separated.")

# -------------------------------------------------------
# Load Preprocessing Objects
# -------------------------------------------------------

preprocessor = load_model(PREPROCESSOR)
label_encoder = load_model(LABEL_ENCODER)

y = label_encoder.transform(y)

logger.info("Preprocessor and Label Encoder loaded.")

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

logger.info("Train-Test split completed.")

# -------------------------------------------------------
# Machine Learning Models
# -------------------------------------------------------

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

# -------------------------------------------------------
# Train Models
# -------------------------------------------------------

best_model = None
best_accuracy = 0.0
best_name = ""

results = []

print("\nTraining Models...\n")

for name, model in models.items():

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    results.append((name, accuracy))

    print(f"{name:<25} Accuracy : {accuracy:.4f}")

    logger.info(f"{name} Accuracy : {accuracy:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = pipeline
        best_name = name

# -------------------------------------------------------
# Save Best Model
# -------------------------------------------------------

save_model(best_model, BEST_MODEL)

logger.info(f"Best Model Saved : {best_name}")

# -------------------------------------------------------
# Display Results
# -------------------------------------------------------

print("\n" + "=" * 70)
print("BEST MODEL")
print("=" * 70)

print(f"Model    : {best_name}")
print(f"Accuracy : {best_accuracy:.4f}")

print("\nBest Model Saved Successfully.")
print("\nModel Training Completed Successfully.")

logger.info("Model Training Completed Successfully.")