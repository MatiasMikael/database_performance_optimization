import os
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = '5_logs/create_tables.log'
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create database connection URL
DB_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Define table creation queries
table_queries = [
    text("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """),
    text("""
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        price NUMERIC(10, 2),
        stock INT
    );
    """),
    text("""
    CREATE TABLE IF NOT EXISTS orders (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        product_id INT REFERENCES products(id),
        quantity INT,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
]

# Create tables
try:
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        database_name = conn.execute(text("SELECT current_database();")).scalar()
        print(f"Connected to database: {database_name}")
        logging.info(f"Connected to database: {database_name}")

        for query in table_queries:
            conn.execute(query)
        message = "Tables created successfully!"
        print(message)
        logging.info(message)
except Exception as e:
    message = f"An error occurred: {e}"
    print(message)
    logging.error(message)