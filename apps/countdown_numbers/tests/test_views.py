from django.urls import reverse

import pytest

pytestmark = pytest.mark.django_db

def test_get_selection_screen(client):
    """ Asserts a site visitor can GET the `selection` screen """
    path = reverse('countdown_numbers:selection')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'

def test_post_selection_screen(client):
    """ Asserts a site visitor can POST from the `selection` screen """
    path = reverse('countdown_numbers:selection')
    data = {'num_from_top': 1}
    response = client.post(path, data)
    assert response.status_code == 302, 'Should return a redirection status code'

def test_form_not_valid(client):
    """ Asserts a site visitor returns to the selection screen """
    path = reverse('countdown_numbers:selection')
    data = {'num_from_top':5}
    response = client.post(path, data)
    assert not response.context['form'].is_valid()
    assert response.context['widget']['attrs']['min'] == 0
    assert response.context['widget']['attrs']['max'] == 4
    assert response.status_code == 200, 'Should return an `OK` status code'

def test_get_game_screen(client):
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
def test_results_screen(client):
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
