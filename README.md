# Employee Attrition Prediction & HR Analytics

An end-to-end Machine Learning project for predicting employee attrition
and providing HR analytics through an interactive Streamlit dashboard.

The project was developed as part of a Machine Learning using Python
internship and follows a complete workflow from data preprocessing and
exploratory data analysis to model training, evaluation, prediction,
business insights, and Streamlit deployment.

## Project Overview

Employee attrition can affect productivity, recruitment costs, workforce
planning, and overall business performance. This project uses the IBM HR
Analytics Employee Attrition dataset to build a classification-based
prediction system.

The application allows a user to enter employee information and receive:

-   Employee attrition prediction
-   Stay probability
-   Leave probability
-   Model confidence score
-   HR recommendations
-   Interactive HR analytics charts

The dataset used in the project contains **1,470 records and 35
features**, with `Attrition` as the target variable.

## Features

### Data Science / Machine Learning

-   Data loading
-   Data cleaning and preprocessing
-   Exploratory Data Analysis (EDA)
-   Data visualization
-   Feature engineering
-   Categorical feature encoding
-   Machine Learning model training
-   Model evaluation
-   Prediction pipeline
-   Saved trained model and preprocessing components

### HR Analytics Dashboard

-   Attrition distribution
-   Department distribution
-   Monthly income distribution
-   Employee age distribution
-   Interactive employee input form
-   Attrition prediction
-   Stay/leave probabilities
-   Confidence score
-   HR recommendations

## Machine Learning Workflow

``` text
IBM HR Analytics Dataset
          ↓
     Data Loading
          ↓
 Data Cleaning & Preprocessing
          ↓
          EDA
          ↓
 Data Visualization
          ↓
   Feature Engineering
          ↓
     Model Training
          ↓
    Model Evaluation
          ↓
   Best Model Selection
          ↓
   Model Serialization
          ↓
 Streamlit Application
          ↓
 Employee Input
          ↓
 Attrition Prediction
          ↓
 Probabilities + Confidence
          ↓
 HR Recommendations
```

## Machine Learning Models

The project evaluates classification algorithms including:

-   Logistic Regression
-   Decision Tree
-   Random Forest
-   Gradient Boosting

The internship report documents Logistic Regression as the final
prediction model used by the application.

Model evaluation includes:

-   Accuracy
-   Precision
-   Recall
-   F1-Score
-   Confusion Matrix
-   Classification Report

The project also documents advanced techniques explored during the
internship, including:

-   GridSearchCV
-   RandomizedSearchCV
-   SMOTE
-   K-Fold cross-validation
-   Stratified K-Fold cross-validation

## Technology Stack

  Technology     Purpose
  -------------- -------------------------------
  Python         Programming
  Pandas         Data processing
  NumPy          Numerical computing
  Matplotlib     Visualization
  Plotly         Interactive charts
  Scikit-learn   Machine Learning
  Joblib         Saving/loading trained models
  Streamlit      Web application/dashboard
  Git            Version control
  GitHub         Source code hosting
  VS Code        Development environment

## Dataset

The project uses the **IBM HR Analytics Employee Attrition** dataset.

Dataset characteristics:

-   Records: 1,470
-   Features: 35
-   Target: `Attrition`
-   Format: CSV
-   Source: Kaggle

Dataset reference:

https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

> If you redistribute the dataset, follow the dataset's applicable terms
> and attribution requirements.

## Project Structure

The project uses a modular structure separating data, trained models,
Python processing modules, outputs, and Streamlit UI components.

``` text
Employee-Attrition-Prediction-ML/
│
├── dataset/
│   └── # Dataset files
│
├── logs/
│   └── # Application/training logs, if generated
│
├── models/
│   └── # Trained model and preprocessing files
│
├── notebooks/
│   └── # Jupyter notebooks
│
├── outputs/
│   └── # Generated charts, reports, and results
│
├── python/
│   ├── config.py
│   ├── utils.py
│   └── # Data processing / ML modules
│
├── ui/
│   ├── styles.py
│   ├── sidebar.py
│   ├── dashboard.py
│   ├── charts.py
│   ├── form.py
│   ├── predictor.py
│   └── recommendation.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

### Important

The trained model and preprocessing files referenced by
`python/config.py` must be included in the GitHub repository if you want
another person to run the Streamlit dashboard without retraining the
model.

The dataset file referenced by the application must also be present in
the expected `dataset/` location.

## Requirements

According to the project report, the project requires:

-   Windows 10/11 or a compatible operating system
-   Python 3.10+
-   Git
-   Internet connection for installing dependencies
-   At least 8 GB RAM recommended
-   Approximately 5 GB storage recommended

The easiest setup is to use the included `requirements.txt`.

------------------------------------------------------------------------

# How to Run the Project

## Method 1 --- Download ZIP and Run

This method allows someone to download the GitHub project as a ZIP file,
extract it, and run it without cloning the repository.

### Step 1: Download the project

On GitHub:

1.  Open the repository.
2.  Click **Code**.
3.  Click **Download ZIP**.
4.  Extract the ZIP file.

After extraction, you should have a folder similar to:

``` text
Employee-Attrition-Prediction-ML/
```

### Step 2: Open the project folder

Open the extracted folder in VS Code.

Or open PowerShell/Command Prompt inside the project folder.

Example:

``` powershell
cd C:\Projects\Employee-Attrition-Prediction-ML
```

### Step 3: Create a virtual environment

It is recommended to create a fresh virtual environment instead of
sharing the developer's existing `venv`.

Windows PowerShell:

``` powershell
python -m venv venv
```

Activate it:

``` powershell
.\venv\Scripts\Activate.ps1
```

You should see:

``` text
(venv) PS C:\Projects\Employee-Attrition-Prediction-ML>
```

If PowerShell blocks activation, run:

``` powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

``` powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

Run:

``` powershell
pip install -r requirements.txt
```

### Step 5: Run the Streamlit application

Run:

``` powershell
streamlit run app.py
```

If the `streamlit` command is not recognized, use:

``` powershell
python -m streamlit run app.py
```

### Step 6: Open the application

Streamlit normally displays:

``` text
Local URL: http://localhost:8501
```

Open:

``` text
http://localhost:8501
```

The Employee Attrition Prediction & HR Analytics dashboard will open in
your browser.

------------------------------------------------------------------------

# Quick Start

For an already-installed Python environment:

``` powershell
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Employee-Attrition-Prediction-ML

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python -m streamlit run app.py
```

Then open:

``` text
http://localhost:8501
```

Replace `<YOUR-GITHUB-REPOSITORY-URL>` with the actual GitHub repository
URL.

------------------------------------------------------------------------

# macOS / Linux

``` bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Employee-Attrition-Prediction-ML

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python -m streamlit run app.py
```

Then open:

``` text
http://localhost:8501
```

------------------------------------------------------------------------

# Running Without Retraining

The Streamlit application is designed to load the prepared dataset and
saved Machine Learning artifacts referenced by the project
configuration.

Therefore, a user does **not** need to retrain the model just to open
the dashboard, provided the required dataset and model/preprocessing
files are included in the repository.

If those files are missing, the application may display an application
error when it starts.

------------------------------------------------------------------------

# How to Use the Dashboard

1.  Start the Streamlit application.
2.  Review the HR analytics dashboard.
3.  Open the employee input section.
4.  Enter employee information such as:
    -   Age
    -   Gender
    -   Department
    -   Job Role
    -   Monthly Income
    -   Overtime
    -   Job Level
    -   Job Satisfaction
    -   Work Experience
    -   Work-Life Balance
    -   Other employee-related attributes
5.  Click **Predict Attrition**.
6.  Review:
    -   Attrition prediction
    -   Stay probability
    -   Leave probability
    -   Confidence score
    -   HR recommendation

------------------------------------------------------------------------

# Troubleshooting

## `streamlit` is not recognized

Run:

``` powershell
python -m streamlit run app.py
```

If Streamlit is not installed:

``` powershell
pip install -r requirements.txt
```

## `ModuleNotFoundError`

Make sure the virtual environment is activated:

``` powershell
.\venv\Scripts\Activate.ps1
```

Then reinstall dependencies:

``` powershell
pip install -r requirements.txt
```

## Application Error while loading model or dataset

Check that:

-   The `dataset/` folder exists.
-   The required dataset file exists.
-   The `models/` folder exists.
-   The trained model files exist.
-   `python/config.py` points to the correct file paths.
-   You are running the command from the project root.

Correct:

``` text
Employee-Attrition-Prediction-ML/
```

Then:

``` powershell
python -m streamlit run app.py
```

Avoid running the application from inside `python/` or `ui/`.

## Port 8501 is already in use

Run Streamlit on another port:

``` powershell
python -m streamlit run app.py --server.port 8502
```

Then open:

``` text
http://localhost:8502
```

------------------------------------------------------------------------

# GitHub Upload Guide

Before uploading the project to GitHub, make sure the repository
contains the source code, required data/model files, `requirements.txt`,
and this README.

### Do NOT upload the virtual environment

Do not upload:

``` text
venv/
```

The virtual environment is machine-specific and can be recreated using:

``` powershell
python -m venv venv
pip install -r requirements.txt
```

### Recommended `.gitignore`

``` gitignore
# Virtual environment
venv/
.venv/

# Python cache
__pycache__/
*.py[cod]

# Jupyter
.ipynb_checkpoints/

# IDE
.vscode/

# OS files
.DS_Store
Thumbs.db

# Secrets
.env
.streamlit/secrets.toml

# Logs
*.log

# Temporary files
*.tmp
*.temp
```

If your project already has a `.gitignore`, keep it and add any missing
entries above.

------------------------------------------------------------------------

# Upload to GitHub Using Git

Open PowerShell in the project root:

``` powershell
git init
```

Add the files:

``` powershell
git add .
```

Create the first commit:

``` powershell
git commit -m "Initial commit - Employee Attrition Prediction HR Analytics"
```

Rename the branch:

``` powershell
git branch -M main
```

Add your GitHub repository:

``` powershell
git remote add origin <YOUR-GITHUB-REPOSITORY-URL>
```

Push the project:

``` powershell
git push -u origin main
```

Replace:

``` text
<YOUR-GITHUB-REPOSITORY-URL>
```

with your actual GitHub repository URL.

------------------------------------------------------------------------

# Important GitHub Checklist

Before pushing, verify:

-   [ ] `app.py` is present
-   [ ] `python/` is present
-   [ ] `ui/` is present
-   [ ] `models/` is present
-   [ ] Required dataset files are present
-   [ ] `requirements.txt` is present
-   [ ] `README.md` is present
-   [ ] `.gitignore` is present
-   [ ] `venv/` is NOT uploaded
-   [ ] `__pycache__/` is NOT uploaded
-   [ ] Personal secrets/API keys are NOT uploaded
-   [ ] The project runs locally with `python -m streamlit run app.py`

------------------------------------------------------------------------

# Development

To modify the project:

``` powershell
.\venv\Scripts\Activate.ps1
python -m streamlit run app.py
```

The main Streamlit entry point is:

``` text
app.py
```

The application imports the Machine Learning configuration/utilities
from `python/` and the dashboard components from `ui/`.

------------------------------------------------------------------------

# Project Output

The completed application provides an interactive HR analytics and
prediction dashboard containing:

-   HR analytics charts
-   Employee input form
-   Attrition prediction
-   Stay probability
-   Leave probability
-   Model confidence
-   HR recommendations

The project report documents the Streamlit dashboard, employee input
form, prediction result, and HR recommendation dashboard as part of the
final application.

------------------------------------------------------------------------

# References

-   IBM HR Analytics Employee Attrition Dataset --- Kaggle
-   Scikit-learn Documentation
-   Streamlit Documentation
-   Pandas Documentation
-   NumPy Documentation
-   Matplotlib Documentation
-   Plotly Python Documentation
-   Joblib Documentation
-   Python Documentation
-   Git Documentation
-   GitHub Documentation

## Official Documentation

-   https://scikit-learn.org/stable/
-   https://docs.streamlit.io/
-   https://pandas.pydata.org/docs/
-   https://numpy.org/doc/
-   https://matplotlib.org/stable/
-   https://plotly.com/python/
-   https://joblib.readthedocs.io/
-   https://docs.python.org/3/
-   https://git-scm.com/doc
-   https://docs.github.com/

------------------------------------------------------------------------

# License

Add the license that applies to your project here.

If you do not intend to grant reuse permissions yet, you can omit a
license file and this section until you decide which license to use.

------------------------------------------------------------------------

## Author

**Employee Attrition Prediction & HR Analytics Using Machine Learning**

Developed using Python, Scikit-learn, Plotly, Joblib, and Streamlit.
