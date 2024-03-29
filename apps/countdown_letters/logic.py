""" Countdown Letters Logic

A collection of classes and functions that are required to implement
the core logic for the Countdown Letters Game.
"""

import os
from collections import Counter
from random import choices, random
from typing import Dict, List, Set

from aa_project.settings.base import APPS_DIR


class GameSetup:
    """
    Sets up a game with the standard attributes of a game as at the
    game's starting point.
    """

    MAX_GAME_LETTERS: int = 9

    @staticmethod
    def get_weighted_vowels() -> List:
        """
        Compiles vowel letters with number of vowels required to produce
        weighted distribution of the various vowels for the game.
        """
        vowel_freq: Dict[str, int] = {
            "A": 15,
            "E": 21,
            "I": 13,
            "O": 13,
            "U": 5,
        }
        s: str = "".join(key * value for key, value in vowel_freq.items())
        return list(s)

    @staticmethod
    def get_weighted_consonants() -> List:
        """
        Compiles consonant letters with the number of consonants
        required to produce the weighted distribution of the various
        consonants for the game.
        """
        consonant_freq: Dict[str, int] = {
            "B": 2,
            "C": 3,
            "D": 6,
            "F": 2,
            "G": 3,
            "H": 2,
            "J": 1,
            "K": 1,
            "L": 5,
            "M": 4,
            "N": 8,
            "P": 4,
            "Q": 1,
            "R": 9,
            "S": 9,
            "T": 9,
            "V": 1,
            "W": 1,
            "X": 1,
            "Y": 1,
            "Z": 1,
        }
        s: str = "".join(key * value for key, value in consonant_freq.items())
        return list(s)


def get_letters_chosen(num_vowels: int) -> str:
    """
    Returns an appropriate proportion of vowels and consonants within
    the randomised game selection according to their frequency of
    existence
    """
    letters_chosen = []

    weighted_vowels = GameSetup.get_weighted_vowels()
    for _ in range(num_vowels):
        vowel_picked = choices(weighted_vowels)
        weighted_vowels.remove(vowel_picked[0])
        letters_chosen.append(vowel_picked)

    weighted_consonants = GameSetup.get_weighted_consonants()
    num_consonants = GameSetup.MAX_GAME_LETTERS - num_vowels
    for _ in range(num_consonants):
        consonant_picked = choices(weighted_consonants)
        weighted_consonants.remove(consonant_picked[0])
        letters_chosen.append(consonant_picked)

    letters_chosen = sorted(letters_chosen, key=lambda k: random())
    return "".join([item for list_item in letters_chosen for item in list_item])


def get_words() -> Set:
    """
    Returns all words from the `words.txt` file as a set
    Source: http://www.mieliestronk.com/corncob_lowercase.txt
    Words > 9 chars in length removed
    """
    words_filename = os.path.join(APPS_DIR, "countdown_letters/words.txt")
    with open(words_filename, "r") as words_file:
        words_set = {word.strip("\n") for word in words_file}
    return words_set


def get_shortlisted_words(words: Set, letters: str) -> List:
    """
    Given a set of words and a string of the game's letters, returns a
    list of accumulatively gathered longest words sorted by word length
    """
    longest_words = {}
    cumulative_max_letter_count = 0
    letters_in_selection = list(letters)
    for tested_word in words:
        letters_in_tested_word = list(tested_word.upper())
        if len(letters_in_tested_word) < len(letters_in_selection):
            common_letters = list(
                (Counter(letters_in_selection) & Counter(letters_in_tested_word)).elements()
            )
            letter_count = len(common_letters)
            if letter_count >= cumulative_max_letter_count and len(tested_word) == len(
                common_letters
            ):
                cumulative_max_letter_count = letter_count
                longest_words[tested_word] = cumulative_max_letter_count
    return sorted(longest_words.items(), key=lambda x: x[1], reverse=True)


def get_longest_possible_word(shortlisted_words: List) -> str:
    """
    Given a shortlisted list of tuples, returns the word at the first
    indexed position
    """
    for item in shortlisted_words:
        longest_possible_word = item[0]
        return longest_possible_word.upper()
    return None


def get_game_score(word_len: int) -> int:
    """Retrieves the game score based on the achieved word length"""
    return word_len * 2 if word_len == 9 else word_len


def get_result(player_word: str, comp_word: str) -> str:
    """Returns the winning player for the game"""
    if len(player_word) > len(comp_word):
        return "You win"
    elif len(player_word) < len(comp_word):
        return "Susie wins"
    return "Draw"
