# Level 6 - Topic 4: Logging
# Better than print() for real applications - has levels, timestamps, file output

import logging

# --- Basic setup ---
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Log levels (lowest to highest severity):
logging.debug("Detailed info for debugging")       # DEBUG
logging.info("General info, app is running")       # INFO
logging.warning("Something unexpected happened")   # WARNING
logging.error("A serious problem occurred")        # ERROR
logging.critical("Program may not continue")       # CRITICAL

# --- Practical example ---
def divide(a, b):
    logging.debug(f"divide({a}, {b}) called")
    if b == 0:
        logging.error("Division by zero attempted!")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logging.info(f"divide({a}, {b}) = {result}")
    return result

try:
    divide(10, 2)
    divide(5, 0)
except ValueError:
    pass

# --- Logging to a file ---
file_logger = logging.getLogger("file_logger")
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.WARNING)
file_logger.addHandler(file_handler)

file_logger.warning("This goes to the file")
file_logger.debug("This won't appear (below WARNING level)")

# --- Module-level logger (best practice) ---
logger = logging.getLogger(__name__)

def process_data(data):
    logger.info(f"Processing {len(data)} items")
    results = [x * 2 for x in data]
    logger.debug(f"Results: {results}")
    return results

process_data([1, 2, 3, 4, 5])

import os
if os.path.exists("app.log"):
    os.remove("app.log")
