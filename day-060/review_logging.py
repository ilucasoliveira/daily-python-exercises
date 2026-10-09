import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def payment(amount):
    logger.info(f"starting payment of {amount}")

    if amount <= 0:
        logger.error(f"invalid amount: {amount}")
        return "failed"

    if amount > 1000:
        logger.warning(f"high amount: {amount}")

    logger.info("payment approved")
    return "approved"


payment(50)
payment(-10)
payment(5000)
