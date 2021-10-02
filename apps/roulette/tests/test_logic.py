import pytest
import requests

from apps.roulette import logic
from apps.roulette.tests.helpers import destinations


def test_places_to_go_dict():
    assert len(logic.Game.places_to_go.keys()) == 12, 'Should be 12 keys in dict'
    assert sum(logic.Game.places_to_go.values()) == 0, "All key's values should be set to zero"


def test_reset_places_to_go():
    logic.Game.places_to_go['Aruba'] = 10
    logic.Game.places_to_go['Barbados'] = 10
    assert logic.Game.places_to_go['Aruba'] == 10 and logic.Game.places_to_go['Barbados'] == 10, \
        '2 keys should have positive integer values'
    for key in logic.Game.places_to_go:
        logic.Game.places_to_go[key] = 0
    assert logic.Game.places_to_go['Aruba'] == 0 and logic.Game.places_to_go['Barbados'] == 0, \
        'The keys should now be back to zero'
    assert sum(logic.Game.places_to_go.values()) == 0, "All key's values should be set to zero"


def test_get_game_result(mocker):
    mocker.patch('time.sleep', return_value=None)
    logic.get_game_result()
    assert len(logic.Game.places_to_go.keys()) == 12, 'Should still be 12 keys in dict'
    assert sum(logic.Game.places_to_go.values()) == 1_000, "Sum of key's values should be 1,000"


@pytest.mark.parametrize(argnames='destinations', argvalues=sorted(destinations))
def test_get_picture_url(destinations):
    pic_url = logic.get_picture_url(destinations)
    assert requests.get(pic_url).status_code == 200, 'Should return an `OK` status'
