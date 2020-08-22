import os

from ab_back_end import settings
from apps.roulette.logging import log_file


def test_log_file_setup():
    assert os.path.join(settings.APPS_DIR, 'roulette/holiday_roulette.log') in log_file
