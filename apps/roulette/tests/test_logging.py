import os

from aa_project.settings import base
from apps.roulette.logging import log_file


def test_log_file_setup():
    assert os.path.join(base.APPS_DIR, 'roulette/holiday_roulette.log') in log_file
