"""
=========================================================
Employee Attrition Prediction & HR Analytics
Main Streamlit Application
=========================================================
"""

# =========================================================
# IMPORT LIBRARIES
# =========================================================

import sys
from pathlib import Path

import streamlit as st

# =========================================================
# PROJECT PATH
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent
PYTHON_FOLDER = PROJECT_ROOT / "python"

if str(PYTHON_FOLDER) not in sys.path:
    sys.path.insert(0, str(PYTHON_FOLDER))

# =========================================================
# IMPORT PROJECT MODULES
# =========================================================

from config import (
    CLEAN_DATASET,
    BEST_MODEL,
    LABEL_ENCODER
)

from utils import (
    load_dataset,
    load_model
)

# =========================================================
# IMPORT UI MODULES
# =========================================================

from ui.styles import load_css
from ui.sidebar import show_sidebar
from ui.dashboard import show_dashboard
from ui.charts import show_charts
from ui.form import employee_form
from ui.predictor import (
    predict_employee,
    show_prediction
)
from ui.recommendation import show_recommendation

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# LOAD CSS
# =========================================================

load_css()

# =========================================================
# LOAD PROJECT FILES
# =========================================================

try:

    df = load_dataset(CLEAN_DATASET)

    model = load_model(BEST_MODEL)

    encoder = load_model(LABEL_ENCODER)

except Exception as e:

    st.error(f"Application Error\n\n{e}")

    st.stop()

# =========================================================
# SIDEBAR
# =========================================================

show_sidebar(df, model)

# =========================================================
# DASHBOARD
# =========================================================

show_dashboard(df, model)

# =========================================================
# CHARTS
# =========================================================

show_charts(df)

# =========================================================
# EMPLOYEE INPUT FORM
# =========================================================

submitted, employee = employee_form()

# =========================================================
# PREDICTION
# =========================================================

if submitted:

    (
        prediction_label,
        stay_probability,
        leave_probability,
        confidence
    ) = predict_employee(
        model,
        encoder,
        employee
    )

    show_prediction(
        prediction_label,
        stay_probability,
        leave_probability,
        confidence
    )

    show_recommendation(
        leave_probability
    )

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center">

### Employee Attrition Prediction & HR Analytics

Built with ❤️ using

**Python • Scikit-Learn • Streamlit • Plotly**

</div>
""",
unsafe_allow_html=True
)