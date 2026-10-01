"""
=========================================================
Employee Attrition Prediction & HR Analytics
Phase 6 : Feature Engineering & Data Preprocessing
=========================================================
Author : Ams
=========================================================
"""

# -------------------------------------------------------
# Import Libraries
# -------------------------------------------------------

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder,
    StandardScaler
)

from config import (
    CLEAN_DATASET,
    PREPROCESSOR,
    LABEL_ENCODER
)

from utils import (
    load_dataset,
    save_model,
    print_heading
)

from logger import logger

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

df = load_dataset(CLEAN_DATASET)

print_heading("FEATURE ENGINEERING & DATA PREPROCESSING")
logger.info("Clean dataset loaded successfully.")

# -------------------------------------------------------
# Features and Target
# -------------------------------------------------------

X = df.drop("Attrition", axis=1)
y = df["Attrition"]

print(f"\nFeature Matrix Shape : {X.shape}")
print(f"Target Shape         : {y.shape}")

# -------------------------------------------------------
# Encode Target Variable
# -------------------------------------------------------

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(y)

print("\nTarget Classes")

for index, value in enumerate(label_encoder.classes_):
    print(f"{index} -> {value}")

logger.info("Target variable encoded successfully.")

# -------------------------------------------------------
# Identify Feature Types
# -------------------------------------------------------

categorical_columns = X.select_dtypes(
    include=["object", "string"]
).columns.tolist()

numerical_columns = X.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

print("\nCategorical Features")
print(categorical_columns)

print("\nNumerical Features")
print(numerical_columns)

logger.info("Feature types identified.")

# -------------------------------------------------------
# Numerical Pipeline
# -------------------------------------------------------

numeric_transformer = Pipeline(
    steps=[
        ("scaler", StandardScaler())
    ]
)

# -------------------------------------------------------
# Categorical Pipeline
# -------------------------------------------------------

categorical_transformer = Pipeline(
    steps=[
        (
            "encoder",
            OneHotEncoder(handle_unknown="ignore")
        )
    ]
)

# -------------------------------------------------------
# Combined Preprocessor
# -------------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numerical_columns),
        ("cat", categorical_transformer, categorical_columns)
    ]
)

logger.info("Preprocessing pipeline created.")

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

print(f"\nTraining Samples : {X_train.shape[0]}")
print(f"Testing Samples  : {X_test.shape[0]}")

logger.info("Train-test split completed.")

# -------------------------------------------------------
# Fit Preprocessor
# -------------------------------------------------------

X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

print(f"\nProcessed Training Shape : {X_train_processed.shape}")
print(f"Processed Testing Shape  : {X_test_processed.shape}")

logger.info("Preprocessing completed successfully.")

# -------------------------------------------------------
# Save Objects
# -------------------------------------------------------

save_model(preprocessor, PREPROCESSOR)
save_model(label_encoder, LABEL_ENCODER)

print("\nPreprocessor Saved Successfully.")
print("Label Encoder Saved Successfully.")

logger.info("Preprocessor saved.")
logger.info("Label encoder saved.")

# -------------------------------------------------------
# Completion
# -------------------------------------------------------

print("\nFeature Engineering Completed Successfully.")

logger.info("Phase 6 completed successfully.")