import logging
from pathlib import Path

import quakewatch as qw

# Create the logs folder if it does not exist
Path("logs").mkdir(parents=True, exist_ok=True)

# Display logs in the terminal and save them to logs/run.log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/run.log", mode="a"),
    ],
    force=True,
)

if "127.0.0.1" in qw.BASE:  # practice copy of the API on this laptop
    import mock_usgs
    mock_usgs.start()

print(qw.run_pipeline())