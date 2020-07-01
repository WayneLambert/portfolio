import logging
import os

from django.conf import settings

log_file = os.path.join(settings.BASE_DIR, 'roulette/holiday_roulette.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="""%(asctime)s.%(msecs)03d %(levelname)-8s %(filename)s %(module)s: \
        %(lineno)d - %(funcName)s: %(message)s""",
    datefmt="%Y-%m-%d %H:%M:%S"
)
