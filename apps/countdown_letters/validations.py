""" Countdown Letters Validations

A collection of functions that are required to validate given answers
within a game.
"""

import requests

from apps.countdown_letters.oxford_api import API


def is_in_oxford_api(word: str) -> bool:
    """
    Given a word, validates that the word exists in the Oxford API.
    """
    url = f"{API.LEMMAS_URL}{word.lower()}"
    response = requests.get(url, headers=API.headers)
    return response.status_code == 200


def is_eligible_answer(answer: str, letters: str) -> bool:
    """
    Given an answer and the game letters, validates that the answer can
    be made from the game letters.
    """
    letters_in_answer = list(answer)
    letters_in_selection = list(letters)
    while letters_in_answer:
        for letter in answer:
            if letter in letters_in_answer and letter in letters_in_selection:
                letters_in_selection.remove(letter)
                letters_in_answer.remove(letter)
            else:
                return False
        return True
