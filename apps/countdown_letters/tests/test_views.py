from django.urls import reverse

import pytest


pytestmark = pytest.mark.django_db(reset_sequences=True)

def test_get_selection_screen(client):
    """ Asserts a site visitor can GET the `selection` screen """
    path = reverse('countdown_letters:selection')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'

@pytest.mark.parametrize(argnames='num_vowels_selected', argvalues=[3, 4, 5])
def test_post_selection_screen(client, num_vowels_selected):
    """ Asserts a site visitor can POST from the `selection` screen """
    path = reverse('countdown_letters:selection')
    data = {'num_vowels_selected': num_vowels_selected}
    response = client.post(path, data)
    assert response.status_code == 302, 'Should return a redirection status code'

@pytest.mark.parametrize(argnames='num_vowels', argvalues=[1, 2, 6, 7])
def test_form_not_valid(client, num_vowels):
    """ Asserts a site visitor returns to the selection screen """
    path = reverse('countdown_letters:selection')
    data = {'num_vowels': num_vowels}
    response = client.post(path, data)
    assert not response.context['form'].is_valid()
    assert response.context['widget']['attrs']['min'] == 3
    assert response.context['widget']['attrs']['max'] == 5
    assert response.status_code == 200, 'Should return an `OK` status code'

def test_get_game_screen(client):
    """ Asserts a site visitor can GET the `game` screen """
    base_path = reverse('countdown_letters:game')
    params = {
        'letters_chosen': 'ABCDEFGHI'
    }
    response = client.get(base_path, params)
    assert response.status_code == 200, 'Should return an `OK` status code'
    assert 'The letters selected' in response.content.decode('utf-8'), \
        'Should contain specified text'

@pytest.mark.vcr()
def test_get_results_screen(client):
    """ Asserts a site visitor can GET the `results` screen """
    path = reverse('countdown_letters:results')
    params = {
        'letters_chosen': 'SWIMMINGS',
        'players_word': 'SWIMMING'
    }
    response = client.get(path, params)
    assert response.status_code == 200, 'Should return an `OK` status code'
    assert 'You found a' in response.content.decode('utf-8'), 'Should contain specified text'
