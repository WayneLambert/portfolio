""" Fixtures to facilitate the testing of the Countdown Numbers app """

import pytest

from mixer.backend.django import mixer

from apps.countdown_numbers.models import NumbersGame


@pytest.fixture(scope='function')
def numbers_game():
    return mixer.blend(NumbersGame, pk=1)
