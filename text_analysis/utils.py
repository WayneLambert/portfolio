""" Text Analysis Utility Functions

A collection of functions that facilitate the processing of text for the
text analysis app.
"""

import re
import string
from typing import List, Tuple, operator


def get_orig_full_text(request) -> str:
    return request.GET['fulltext'].strip()


def get_cleaned_full_text(request) -> str:
    return re.sub('[!@#.,/\';]', '', get_orig_full_text(request).lower())


def get_word_list(cleaned_full_text: str) -> List[str]:
    return cleaned_full_text.split()


def get_sorted_words(word_list: list) -> List[Tuple[str, int]]:
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)


def get_letter_counts(cleaned_full_text: str) -> List[str]:
    ALPHABET = string.ascii_lowercase
    letter_counts = []
    total_num_chars = len(cleaned_full_text)
    for letter in ALPHABET:
        char_count = cleaned_full_text.count(letter)
        perc = char_count / total_num_chars * 100
        letter_count_str = f"{letter}: {char_count} ({round(perc, 1)}%)"
        letter_counts.append(letter_count_str.strip('\n'))

    return letter_counts
