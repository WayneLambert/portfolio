""" Functions to facilitate the marking of `slow` unit tests

Adding a `--runslow` flag to a PyTest test run will also run all tests
that are marked with the `slow` decorator.
"""

import pytest


def pytest_addoption(parser):
    """ Sets a command line flag `--runslow` for the CLI """
    parser.addoption(
        '--runslow', action='store_true', default=False, help='run slow tests'
    )


def pytest_configure(config):
    """
    Sets tests with the @pytest.mark.slow decorator as the ones to be
    skipped
    """
    config.addinivalue_line('markers', 'slow: mark test as slow to run')


def pytest_collection_modifyitems(config, items):
    """
    Adds `slow` marker upon collection of tests to run
    """
    if config.getoption('--runslow'):
        return
    skip_slow = pytest.mark.skip(reason='need --runslow option to run')
    for item in items:
        if 'slow' in item.keywords:
            item.add_marker(skip_slow)
