import logging
import os

from django.conf import settings


log_file = os.path.join(settings.APPS_DIR, 'roulette/holiday_roulette.log')

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    encoding='utf-8',
    format="%(asctime)s.%(msecs)03d %(filename)s: %(lineno)d - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
