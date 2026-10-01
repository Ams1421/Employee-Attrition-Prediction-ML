"""
=========================================================
Employee Attrition Prediction & HR Analytics
Logging Configuration
=========================================================
"""

import logging
from pathlib import Path

# ---------------------------------------------------------
# CREATE LOG DIRECTORY
# ---------------------------------------------------------

LOG_DIR = Path("logs")

LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "project.log"

# ---------------------------------------------------------
# LOGGER CONFIGURATION
# ---------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("EmployeeAttrition")