import hypothesis.strategies as st
import pytest
from hypothesis import given

from apps.countdown_letters import logic


class TestGameSetup:
    def test_get_weighted_vowels(self, expected_vowels_list: list):
        """
        Tests the vowels returned from the function matches the actual
        allocation of each vowel according to the rules of the game.
        """
        assert isinstance(expected_vowels_list, list), "Fixture should be a list"
        function_vowels_list = logic.GameSetup.get_weighted_vowels()
        assert isinstance(function_vowels_list, list), "Should be a list instance"
        assert expected_vowels_list == function_vowels_list, "Vowels list should meet game's rules"

    def test_get_weighted_consonants(self, expected_consonants_list: list):
        """
        Tests the consonants returned from the function matches the
        actual allocation of each consonant according to the rules
        of the game.
        """
        assert isinstance(expected_consonants_list, list), "Fixture should be a list"
        function_consonants_list = logic.GameSetup.get_weighted_consonants()
        assert isinstance(function_consonants_list, list)
        assert (
            expected_consonants_list == function_consonants_list
        ), "Consonants list should meet game's rules"


@pytest.mark.parametrize(argnames="num_vowels", argvalues=[3, 4, 5])
def test_get_letters_chosen(num_vowels):
    """
    Test that the letter chosen function returns an appropriate string
    of letters based upon the player's chosen number of vowels.
    """
    letters_chosen = logic.get_letters_chosen(num_vowels)
    vowels = ["A", "E", "O", "I", "U"]
    num_of_vowels, num_of_consontants = 0, 0
    for letter in letters_chosen:
        for vowel in vowels:
            if letter == vowel:
                num_of_vowels += 1
            else:
                num_of_consontants += 1

    assert num_vowels == num_of_vowels
    assert len(letters_chosen) == 9
    assert isinstance(letters_chosen, str)


def test_get_words():
    """
    Asserts the set is populated with all 113,809 words.
    This should be the case because the `words.txt` file is a file of
    unique words by default.
    """
    words = logic.get_words()
    assert isinstance(words, set), "Should be a set"
    assert len(words) == 40_424, "Should have 40,424 words"


def test_get_shortlisted_words():
    """Asserts the shortlisted words dict has at least one key"""
    words = logic.get_words()
    assert isinstance(words, set), "First input to get_shortlisted_words() should be a set"
    shortlisted_words = logic.get_shortlisted_words(words, "AEIBCDFGH")
    assert isinstance(shortlisted_words, list)
    assert len(shortlisted_words) >= 1, "Should have at least one element"


def test_get_longest_possible_word(shortlisted_words: list):
    """Asserts one of the longest possible words is a string"""
    longest_possible_word = logic.get_longest_possible_word(shortlisted_words)
    assert isinstance(shortlisted_words, list), "Fixture should be set up correctly as a list"
    assert longest_possible_word, "Should exist"
    assert len(longest_possible_word) <= 9, "Should be less than or equal to 9 characters"
    assert isinstance(longest_possible_word, str), "Should be a string"
    assert longest_possible_word.isupper, "Should be uppercase"


@given(word_len=st.integers(min_value=1, max_value=9))
def test_get_game_score(word_len: int):
    """Asserts the correct game score is returned"""
    game_score = logic.get_game_score(word_len)
    if word_len == 9:
        assert game_score == 18
    else:
        assert game_score == word_len
    assert isinstance(game_score, int)


def test_get_result():
    """
    Asserts the correct string is returned based upon the possibilities
    of the achieved word lengths for the player and the computer. At
    this stage, the words have been validated for eligibility.
    """
    result = logic.get_result(player_word="this", comp_word="the")
    assert result == "You win"

    result = logic.get_result(player_word="the", comp_word="this")
    assert result == "Susie wins"

    result = logic.get_result(player_word="the", comp_word="the")
    assert result == "Draw"
