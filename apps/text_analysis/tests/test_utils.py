from typing import List, Tuple

# pylint: disable=redefined-outer-name
import pytest

from apps.text_analysis import utils


def test_get_word_list(text_to_analyse):
    word_list = utils.get_word_list(text_to_analyse)
    assert isinstance(word_list, list), 'Should be a list'
    assert len(word_list) == 100, 'Should be 100 words in length'


def test_get_sorted_words(text_to_analyse):
    words_to_sort_list = text_to_analyse.split()
    sorted_words = utils.get_sorted_words(words_to_sort_list)
    assert isinstance(sorted_words, List), 'Should be a list'
    assert isinstance(sorted_words[0], Tuple), 'Elements within the list should be tuples'
    assert len(sorted_words) == 2, 'Should return 2 words. 1 for `lorem` and 1 for `ipsum`'


def test_get_letter_counts(text_to_analyse):
    letter_counts = utils.get_letter_counts(text_to_analyse)
    assert isinstance(letter_counts, list), 'Should be a list'
    assert len(letter_counts) == 26, \
        'Should be 26 items in the list - 1 for each letter of the alphabet'
