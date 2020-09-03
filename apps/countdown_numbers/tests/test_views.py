# pylint: disable=redefined-outer-name
import pytest

from django.urls import reverse


pytestmark = pytest.mark.django_db

def test_get_selection_screen_view(client):
    """ Asserts a site visitor can GET the `selection` screen """
    path = reverse('countdown_numbers:selection')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'

def test_get_game_screen_view(client):
    """ Asserts a site visitor can GET the `game` screen """
    base_path = reverse('countdown_numbers:game')
    get_params = {
        'target_number': '869',
        'numbers_chosen': '[100, 1, 2, 3, 4, 5]'
    }
    response = client.get(base_path, get_params)
    assert response.status_code == 200, 'Should return an `OK` status code'
    assert 'The target number' in response.content.decode('utf-8'), 'Should contain specified text'

@pytest.mark.slow(
    reason='Processing the view also encapsulates game logic, validations, and calculations')
@pytest.mark.django_db
def test_get_results_screen_view(client):
    """ Asserts a site visitor can GET the `results` screen """

    path = reverse('countdown_numbers:results')
    get_params = {
        'target_number': '869',
        'numbers_chosen': '[100, 1, 2, 3, 4, 5]',
        'players_calculation': '100*(5+4)',
    }
    response = client.get(path, get_params)
    assert response.status_code == 200, 'Should return an `OK` status code'
    assert 'Your Calculation' in response.content.decode('utf-8'), 'Should contain specified text'

@pytest.mark.skip(reason='TODO: To be developed')
@pytest.mark.slow(
    reason='Processing the view also encapsulates game logic, validations, and calculations')
@pytest.mark.django_db
def test_returns_user_to_game_screen_view(client):
    """ Asserts a site visitor is returned to the `game` screen when
        they enter the form without submitting a calculation """

    path = reverse('countdown_numbers:results')
    get_params = {
        'target_number': '869',
        'numbers_chosen': '[100, 1, 2, 3, 4, 5]',
        'players_calculation': '',
    }
    response = client.get(path, get_params)
    assert response.status_code == 302, 'Should be redirected back to the `game` screen'
