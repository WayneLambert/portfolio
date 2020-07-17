# pylint: disable=redefined-outer-name
import pytest
from django.urls import reverse


def test_get_selection_screen_view(client, request):
    """ Asserts a site visitor can GET the `selection` screen """
    path = reverse('countdown_letters:selection')
    response = client.get(path)
    assert response.status_code == 200, 'Should return with an `OK` status code'

def test_get_game_screen_view(client, request):
    """ Asserts a site visitor can GET the `game` screen """
    base_path = reverse('countdown_letters:game')
    get_params = {
        'letters_chosen': 'ABCDEFGHI'
    }
    response = client.get(base_path, get_params)
    assert response.status_code == 200, 'Should return with an `OK` status code'
    assert 'The letters selected' in response.content.decode('utf-8'), \
        'Should contain specified text'


@pytest.mark.slow(
    reason='Processing the view also retrieves word defintions from the Oxford Online API')
def test_get_results_screen_view(client, request):
    """ Asserts a site visitor can GET the `results` screen """
    path = reverse('countdown_letters:results')
    get_params = {
        'letters_chosen': 'ABCDEFGHI',
        'players_word': 'CAGE'
    }
    response = client.get(path, get_params)
    assert response.status_code == 200, 'Should return with an `OK` status code'
    assert 'You found a' in response.content.decode('utf-8'), \
        'Should contain specified text'
