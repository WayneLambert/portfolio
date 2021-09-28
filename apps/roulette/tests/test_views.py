from django.urls import reverse


def test_game_screen(client):
    """ Asserts a site visitor can access the `game` screen """
    path = reverse('roulette:game')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'


def test_destination_screen(client, mocker):
    """ Asserts a site visitor can access the `destination` screen """
    mocker.patch('time.sleep', return_value=None)
    path = reverse('roulette:destination')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'


def test_view_log_file_contents(client):
    """ Asserts a site visitor can access the `log file contents` screen """
    path = reverse('roulette:log_file')
    response = client.get(path)
    assert response.status_code == 200, 'Should return an `OK` status code'
