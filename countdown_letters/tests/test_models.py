import pytest
from django.db import models
from mixer.backend.django import mixer

from countdown_letters.models import LettersGame

pytestmark = pytest.mark.django_db


class TestLettersGame:
    def test_single_letters_game_saves(self):
        game = mixer.blend(LettersGame)
        assert game.pk == 1, 'Should create a `Letters Game` instance'

    def test_multi_letters_game_saves(self):
        games = mixer.cycle(10).blend(LettersGame)
        assert games[9].pk == 10, '10th instance should have a PK of 10'
        assert LettersGame.objects.count() == 10, 'Should have 10 objects in the database'

    def test_can_delete_letters_game(self):
        games = mixer.cycle(10).blend(LettersGame)
        games[4].delete()
        assert LettersGame.objects.count() == 9, 'Should have 9 objects remaining in the database'

    def test_letters_chosen_is_charfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("letters_chosen")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_players_word_is_charfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("players_word")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_comp_word_is_charfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("comp_word")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_eligible_answer_is_charfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("eligible_answer")
        assert isinstance(field, models.BooleanField), 'Should be a boolean field'

    def test_winning_word_is_charfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("winning_word")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_player_word_len_is_integerfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("player_word_len")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_comp_word_len_is_integerfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("comp_word_len")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_player_score_is_integerfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("player_score")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_comp_score_is_integerfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("comp_score")
        assert isinstance(field, models.IntegerField), 'Should be an integer field'

    def test_definition_is_textfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("definition")
        assert isinstance(field, models.TextField), 'Should be a text field'

    def test_word_class_is_charfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("word_class")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_result_is_charfield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("result")
        assert isinstance(field, models.CharField), 'Should be a char field'

    def test_entry_date_is_datefield(self):
        game = mixer.blend(LettersGame)
        field = game._meta.get_field("entry_date")
        assert isinstance(field, models.DateField), 'Should be a date field'
