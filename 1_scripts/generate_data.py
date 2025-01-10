import os
import random
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
LOG_FILE = '5_logs/generate_data.log'
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

# Generate data
try:
    with engine.connect() as conn:
        # Generate users
        users = [(f"User{i}", f"user{i}@example.com") for i in range(1, 1001)]
        conn.execute(text("INSERT INTO users (name, email) VALUES (:name, :email)"), [{'name': u[0], 'email': u[1]} for u in users])
        logging.info("1000 users added successfully.")

        # Generate products
        products = [(f"Product{i}", round(random.uniform(5.0, 100.0), 2), random.randint(1, 50)) for i in range(1, 201)]
        conn.execute(text("INSERT INTO products (name, price, stock) VALUES (:name, :price, :stock)"), [{'name': p[0], 'price': p[1], 'stock': p[2]} for p in products])
        logging.info("200 products added successfully.")

        # Fetch valid IDs
        user_ids = [row[0] for row in conn.execute(text("SELECT id FROM users"))]
        product_ids = [row[0] for row in conn.execute(text("SELECT id FROM products"))]

        # Generate orders
        orders = []
        for _ in range(10000):
            user_id = random.choice(user_ids)
            product_id = random.choice(product_ids)
            quantity = random.randint(1, 5)
            orders.append({'user_id': user_id, 'product_id': product_id, 'quantity': quantity})
        conn.execute(text("INSERT INTO orders (user_id, product_id, quantity) VALUES (:user_id, :product_id, :quantity)"), orders)
        logging.info("10000 orders added successfully.")

        # Log success
        message = "Test data generated successfully with 10,000 orders!"
        print(message)
        logging.info(message)

except Exception as e:
    message = f"An error occurred while generating data: {e}"
    print(message)
    logging.error(message)