import pytest
from django.db import models
from mixer.backend.django import mixer

from countdown_numbers.models import NumbersGame

pytestmark = pytest.mark.django_db


class TestNumbersGame:
    def test_single_numbers_game_saves(self):
        game = mixer.blend(NumbersGame)
        assert game.pk == 1, 'Should create a `Numbers Game` instance'

    def test_multi_numbers_game_saves(self):
        games = mixer.cycle(10).blend(NumbersGame)
        assert games[9].pk == 10, '10th instance should have a PK of 10'
        assert NumbersGame.objects.count() == 10, 'Should have 10 objects in the database'

    def test_can_delete_numbers_game(self):
        games = mixer.cycle(10).blend(NumbersGame)
        games[4].delete()
        assert NumbersGame.objects.count() == 9, 'Should have 9 objects remaining in the database'

    def test_game_nums_is_charfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("game_nums")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_target_number_is_integerfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("target_number")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_player_num_achieved_is_integerfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("player_num_achieved")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_valid_calc_is_booleanfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("valid_calc")
        assert isinstance(field, models.BooleanField), 'Should be a boolean field'

    def test_comp_num_achieved_is_integerfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("comp_num_achieved")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_player_score_is_integerfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("player_score")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_comp_score_is_integerfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("comp_score")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_solution_str_is_charfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("solution_str")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_game_result_is_charfield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("game_result")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_entry_date_is_datefield(self):
        game = mixer.blend(NumbersGame)
        field = game._meta.get_field("entry_date")
        assert isinstance(field, models.DateField), 'Should be a date field'
