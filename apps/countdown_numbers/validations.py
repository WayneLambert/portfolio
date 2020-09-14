""" Functions required to validate given answers within a game. """

import ast
import re

from collections import namedtuple

from django.contrib import messages


def check_chars(players_calc: str) -> bool:
    """
    Checks that the characters entered by the player are valid.
    - If valid, the game's processing logic continues.
    - If invalid, help message is displayed to the player.
    """
    pattern = r'^[0-9()\+\-\*\/]*$'
    match_set = re.search(pattern, players_calc)
    return match_set is not None


def check_brackets(players_calc: str) -> bool:
    """ Checks there's a matching number of opening/closing brackets """
    return players_calc.count('(') == players_calc.count(')')


def check_legal_chars_seq(players_calc: str) -> bool:
    """
    Checks for known illegal character sequences entered by the player.
    - If valid, the game's processing logic continues.
    - If invalid, help message is displayed to the player.
    """
    patterns = ['+)', '-)', '*)', '/)']
    return all(pattern not in players_calc for pattern in patterns)


def strip_spaces(players_calc: str) -> str:
    """ Removes unncessary spaces within a player's answer. """
    return players_calc.replace(' ', '')


def calc_entered_is_valid(players_calc: str) -> namedtuple:
    """ Validates the calc entered is in a valid format. """
    players_calc = strip_spaces(players_calc)
    has_valid_chars = check_chars(players_calc)
    has_valid_brackets = check_brackets(players_calc)
    has_valid_sequences = check_legal_chars_seq(players_calc)

    ValidCalc = namedtuple(
        'ValidCalc', ['has_valid_chars', 'has_valid_brackets', 'has_valid_sequences'])
    return ValidCalc(has_valid_chars, has_valid_brackets, has_valid_sequences)


def output_message(request, checks: namedtuple):
    """ When checks do not pass, displays a message to the player """
    msg: str = ""
    if not checks.has_valid_brackets:
        msg = "There is a mismatch in the number of opening and closing brackets used."
    
    if not checks.has_valid_chars:
        msg = "Only arithmetic operators, digits, and rounded brackets are permitted characters."
    
    if not checks.has_valid_sequences:
        msg = (f"The string sequence is an invalid one. " +
                "Please check the calculation string and resubmit.")

    messages.add_message(request, messages.INFO, msg)


def get_permissible_nums(request) -> list:
    """ Returns list of numbers used to form a valid calc """
    return ast.literal_eval(request.GET.get('numbers_chosen'))


def get_nums_used(players_calc: str) -> list:
    """ Returns list of numbers used to form player's calc """
    nums_used = re.split(r'; |, |\*|\/|\+|\-|\(|\)', players_calc)
    nums_used[:] = (int(item) for item in nums_used if item != '')
    return nums_used


def is_calc_valid(request, players_calc) -> bool:
    """ Validates numbers used for player's calc are permissible """
    players_calc = strip_spaces(players_calc)
    nums_used = get_nums_used(players_calc)
    permissible_nums = get_permissible_nums(request)
    for test_num in nums_used:
        if test_num not in permissible_nums:
            return False
        permissible_nums.remove(test_num)
    return True
