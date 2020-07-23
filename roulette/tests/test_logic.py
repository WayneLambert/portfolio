import pytest
import requests

from roulette import logic
from roulette.tests.helpers import destinations


def test_places_to_go_dict():
    assert len(logic.places_to_go.keys()) == 12, 'Should be 12 keys in dict'
    assert sum(logic.places_to_go.values()) == 0, "All key's values should be set to zero"


def test_reset_places_to_go():
    logic.places_to_go['Aruba'] = 10
    logic.places_to_go['Barbados'] = 10
    assert logic.places_to_go['Aruba'] == 10 and logic.places_to_go['Barbados'] == 10, \
        '2 keys should have positive integer values'
    for key in logic.places_to_go:
        logic.places_to_go[key] = 0
    assert logic.places_to_go['Aruba'] == 0 and logic.places_to_go['Barbados'] == 0, \
        'The keys should now be back to zero'
    assert sum(logic.places_to_go.values()) == 0, "All key's values should be set to zero"


@pytest.mark.slow(reason='Function has 1,000 iterations at 0.003/secs each (3 secs overall)')
def test_get_roulette_result():
    result = logic.get_roulette_result()
    assert len(logic.places_to_go.keys()) == 12, 'Should still be 12 keys in dict'
    assert sum(logic.places_to_go.values()) == 1_000, "Sum of key's values should be 1,000"


@pytest.mark.parametrize(argnames='destinations', argvalues=destinations)
def test_get_picture_url(destinations):
    pic_url = logic.get_picture_url(destinations)
    assert requests.get(pic_url).status_code == 200, 'Should return an `OK` status'
