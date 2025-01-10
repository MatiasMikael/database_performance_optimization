import os
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = '5_logs/test_connection.log'
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create database connection URL
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Test the connection
try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        message = "Connection to the database is successful!"
        print(message)
        logging.info(message)
except Exception as e:
    message = f"Connection failed: {e}"
    print(message)
    logging.error(message)