# Setting Up the Logging

import os
import sys
import logging

# We are gonna log each and every detail using generic logging structure

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format= logging_str,

    handlers= [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)  #stream handler helps us to see the output message we have in the log_filepath when we use terminal
    ]
)

logger = logging.getLogger("End-to-End-DS-Project")

