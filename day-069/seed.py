import logging

from database import SessionLocal, Stock

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

with SessionLocal() as session:
    stock_items = [
        Stock(name="apple", quantity=10),
        Stock(name="banana", quantity=20),
        Stock(name="orange", quantity=30),
    ]
    session.add_all(stock_items)
    session.commit()
    logger.info("Stock items added successfully.")
