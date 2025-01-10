import os
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = '5_logs/create_indexes.log'
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create database connection URL
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Connect to the database
engine = create_engine(DB_URL)

# Define index creation queries
index_queries = [
    "CREATE INDEX IF NOT EXISTS idx_quantity ON orders (quantity);",
    "CREATE INDEX IF NOT EXISTS idx_user_id ON orders (user_id);",
    "CREATE INDEX IF NOT EXISTS idx_product_id ON orders (product_id);"
]

# Create indexes
try:
    with engine.connect() as conn:
        for query in index_queries:
            conn.execute(text(query))
            logging.info(f"Executed: {query}")
        print("Indexes created successfully!")
        logging.info("Indexes created successfully!")
except Exception as e:
    message = f"An error occurred while creating indexes: {e}"
    print(message)
    logging.error(message)