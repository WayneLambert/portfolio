# pylint: disable=redefined-outer-name
from django.urls import reverse

import pytest


def test_game_screen(client):
    """ Asserts a site visitor can GET the `game` screen """
    path = reverse('roulette:holiday_roulette')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'


@pytest.mark.slow(reason='Function has 1,000 iterations at 0.003/secs each (3 secs overall)')
def test_destination_screen(client):
    """ Asserts a site visitor can GET the `destination` screen """
    path = reverse('roulette:holiday_destination')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'


def test_view_log_file_contents(client):
    """ Asserts a site visitor can GET the `log file contents` screen """
    path = reverse('roulette:destination_log_file')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'
