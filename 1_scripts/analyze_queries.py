import os
import random
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = '5_logs/analyze_queries.log'
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

# Define queries to analyze
queries = [
    "SELECT * FROM users;",
    "SELECT * FROM products;",
    "SELECT * FROM orders WHERE quantity > 2;",
    "SELECT u.name, p.name AS product_name, o.quantity FROM orders o \
     JOIN users u ON o.user_id = u.id \
     JOIN products p ON o.product_id = p.id \
     WHERE o.quantity > 3;"
]

# Analyze queries
try:
    with engine.connect() as conn:
        for query in queries:
            logging.info(f"Analyzing query: {query}")
            print(f"Analyzing query: {query}")

            explain_query = f"EXPLAIN (ANALYZE, BUFFERS) {query}"
            result = conn.execute(text(explain_query))
            analysis = "\n".join([row[0] for row in result])

            print(f"Query analysis:\n{analysis}\n")
            logging.info(f"Query analysis:\n{analysis}\n")

except Exception as e:
    message = f"An error occurred while analyzing queries: {e}"
    print(message)
    logging.error(message)