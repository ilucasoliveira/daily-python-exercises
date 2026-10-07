# Day 59 - paper practice: logging (register what happens in the app)
# print does not say WHEN, nor the SEVERITY, and cannot be turned on/off by level.
# logging is the professional way to register events: with time, level and message.

# Log levels (least to most severe):
# DEBUG    - details for debugging
# INFO     - normal events
# WARNING  - something odd but did not break
# ERROR    - something failed
# CRITICAL - severe failure that can bring everything down

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def process_payment(amount):
    logger.info(f"processing payment of {amount}")
    if amount <= 0:
        logger.error("invalid amount")
        return
    if amount > 10000:
        logger.warning("high value payment")
    logger.info("payment processed")


process_payment(100)
process_payment(0)
process_payment(10001)
process_payment(9999)
