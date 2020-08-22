import logging
import os

from ab_back_end.settings import APPS_DIR

log_file = os.path.join(APPS_DIR, 'roulette/holiday_roulette.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="""%(asctime)s.%(msecs)03d %(levelname)-8s %(filename)s %(module)s: \
        %(lineno)d - %(funcName)s: %(message)s""",
    datefmt="%Y-%m-%d %H:%M:%S"
)
