"""Countdown Letters Logic

A collection of classes and functions that are required to implement
the core logic for the Countdown Letters Game.

"""

import array
import os
from random import choices, random
from typing import Dict, Union

import requests
from django.conf import settings

from .oxford_api import API
from .validations import is_in_oxford_api


class GameSetup:
    """
    Sets up a game with the standard attributes of a game as at the
    game's starting point.
    """
    MAX_GAME_LETTERS: int = 9

    @staticmethod
    def get_weighted_vowels():
        """
        Creates a list of vowel letters with the number of vowels
        required to produce the weighted distribution of the various
        vowels for the game.
        """
        vowel_freq: Dict[str, int] = {
            'A': 15,
            'E': 21,
            'I': 13,
            'O': 13,
            'U': 5,
        }
        s: str = ''
        for key, value in vowel_freq.items():
            s += key * value
        return list(s)

    @staticmethod
    def get_weighted_consonants():
        """
        Creates a list of consonant letters with the number of consonants
        required to produce the weighted distribution of the various
        consonants for the game.
        """
        consonant_freq: Dict[str, int] = {
            'B': 2,
            'C': 3,
            'D': 6,
            'F': 2,
            'G': 3,
            'H': 2,
            'J': 1,
            'K': 1,
            'L': 5,
            'M': 4,
            'N': 8,
            'P': 4,
            'Q': 1,
            'R': 9,
            'S': 9,
            'T': 9,
            'V': 1,
            'W': 1,
            'X': 1,
            'Y': 1,
            'Z': 1,
        }
        s: str = ''
        for key, value in consonant_freq.items():
            s += key * value
        return list(s)


def get_letters_chosen(num_vowels: int) -> str:
    """
    Returns an appropriate proportion of vowels and consonants within the randomised
    game selection according to their frequency of existence
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
    return ''.join([item for list_item in letters_chosen for item in list_item])


def get_words() -> tuple:
    """ Retrieves all words from the `words.txt` file """
    words_array = array.array
    words_filename = os.path.join(settings.BASE_DIR, 'countdown_letters/words.txt')
    with open(words_filename, 'r') as words_file:
        words_array = [word.strip('\n') for word in words_file]
    return tuple(words_array)


def get_shortlisted_words(words: tuple, letters: str) -> dict:
    """
    Given a tuple of words and a string of the game's letters, returns
    a shortlist of the accumulatively gathered longest words in the
    running order of cycling through `words.txt`
    """
    shortlisted_words = {}
    cumulative_max_letter_count = 0
    letters_in_selection = list(letters)
    for tested_word in words:
        letters_in_tested_word = list(tested_word.upper())
        if len(letters_in_tested_word) < len(letters_in_selection):
            common_letters = set(letters_in_selection).intersection(
                letters_in_tested_word)
            letter_count = len(common_letters)
            if letter_count >= cumulative_max_letter_count and len(
                    tested_word) == len(common_letters):
                cumulative_max_letter_count = letter_count
                shortlisted_words[tested_word] = cumulative_max_letter_count
    return shortlisted_words


def get_longest_possible_word(shortlisted_words: dict) -> str:
    """
    Given a shortlisted dict of words, returns the word at the
    first indexed position
    """
    sorted_list = sorted(shortlisted_words.items(), reverse=True)
    for item in sorted_list:
        if is_in_oxford_api(item[0]):
            longest_possible_word = item[0]
            return longest_possible_word.upper()


def get_game_score(word_len: int) -> int:
    """ Retrieves the game score based on the achieved word length """
    return word_len ** 2 if word_len == 9 else word_len


def get_lemmas_response_json(word: str) -> dict:
    """ Returns lemmas data component of input word from Oxford Online API """
    lemmas_url = f"{API.OD_API_BASE_URL}{'lemmas/'}{API.LANGUAGE}{'/'}{word.lower()}"
    lemmas_response = requests.get(lemmas_url, headers=API.headers)
    return lemmas_response.json()


def get_alt_word(word: str) -> str:
    """
    Retrieves alternative word to the exact winning word since its singular
    form may be the actual referenced word in the Oxford definitions' API.
    """
    lemmas_json = get_lemmas_response_json(word)
    alt_word_lookup = lemmas_json['results'][0]['lexicalEntries'][0]
    alt_word_lookup = alt_word_lookup['inflectionOf'][0]['id']
    return alt_word_lookup


def lookup_definition(word: str) -> dict:
    """
    Retrieve dictionary definition of winning word using 'Oxford Dictionaries API'.
    An alternative form of the word is used if the Oxford API does not return a
    definition for the exact match of the winning form. In this case, it returns a
    result from the lemmas query.
    """
    definitions_url = f"{API.OD_API_BASE_URL}{'entries/'}{API.LANGUAGE}{'/'}{word.lower()}"
    definitions_response = requests.get(definitions_url, headers=API.headers)
    if definitions_response.status_code == 200:
        definitions_response_json = definitions_response.json()
        definition = definitions_response_json['results'][0]['lexicalEntries'][0]
        word_class = definition['lexicalCategory']['text']
        try:
            definition = definition['entries'][0]['senses'][0]['definitions'][0].capitalize()
        except KeyError:
            definition = f"""The definition for '{word}' cannot be found
                             in the Oxford Dictionary API."""
        alt_word_lookup = word
    else:
        alt_word_lookup = get_alt_word(word)
        definition = lookup_definition(alt_word_lookup)
        lemmas_json = get_lemmas_response_json(word)
        word_class = lemmas_json['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']

    definition_result = {
        'alt_word_lookup': alt_word_lookup,
        'definition': definition,
        'word_class': word_class,
    }

    return definition_result


def present_definition(definition_result: dict) -> Union[dict, str]:
    """
    Given a definition from the Oxford Online API, returns a presentable
    format of the definition that can be rendered within a template
    """
    if isinstance(definition_result['definition'], dict):
        return definition_result['definition']['definition']
    return definition_result['definition']


def get_result(player_word: str, comp_word: str) -> str:
    """ Returns the winning player for the game """
    if len(player_word) > len(comp_word):
        return 'You win'
    if len(player_word) < len(comp_word):
        return 'Susie wins'
    return 'Draw'
