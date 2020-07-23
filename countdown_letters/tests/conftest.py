"""
A set of fixtures to facilitate the testing of the Countdown Letters app
"""

import pytest

@pytest.fixture(scope='function')
def expected_vowels_list() -> list:
    return [
        'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
        'A', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
        'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'I', 'I', 'I', 'I', 'I', 'I',
        'I', 'I', 'I', 'I', 'I', 'I', 'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O', 'O', 'U', 'U', 'U', 'U', 'U'
    ]

@pytest.fixture(scope='function')
def expected_consonants_list() -> list:
    return [
        'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'F', 'F', 'G',
        'G', 'G', 'H', 'H', 'J', 'K', 'L', 'L', 'L', 'L', 'L', 'M', 'M', 'M',
        'M', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'P', 'P', 'P', 'P', 'Q',
        'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'S',
        'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'V',
        'W', 'X', 'Y', 'Z'
    ]


@pytest.fixture(scope='function')
def shortlisted_words() -> list:
    return [
        ('strode', 6),
        ('stored', 6),
        ('droves', 6),
        ('strove', 6),
        ('voters', 6),
        ('doters', 6),
        ('troves', 6),
        ('stover', 6),
        ('sorted', 6),
        ('roves', 5),
        ('redos', 5),
        ('overs', 5),
        ('revs', 4),
        ('rode', 4)
    ]


@pytest.fixture(scope='function')
def given_answers_list() -> list:
    return [
        'sorted', 'tree', 'sort', 'strove',  # Should all return True
        'sarted', 'traa', 'sart', 'strave',  # Should all return False
    ]