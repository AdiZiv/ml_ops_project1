import os
from dotenv import load_dotenv

load_dotenv()

# File paths
FILE_PATH = 'data/database_input.csv'

# Database settings
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'mlops_db')
DB_USER = os.getenv('DB_USER', 'mlops_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'mlops_password')

# Transform settings
FILLNA_TOTALCHARGES = 2279
FILLNA_TOTALCHARGES_STR = '2279'
FILLNA_PhoneService = 'No'

# Model settings
MODEL_PATH = 'models/churn_model.pickle'
MODEL_COLUMNS = ['TotalCharges','Month-to-month','One year','Two year','PhoneService','tenure']

# Data loading settings
LOAD_INITIAL_DATA = True  # Set to False after initial data load

# load
RESULT_FILE_PATH = 'data/result.csv'

