""" Countdown Numbers Validations

A collection of functions that are required to validate
given answers within a game.

"""

import ast
import re

from django.contrib import messages


def check_chars(request, players_calc: str) -> bool:
    """
    Checks that the characters entered by the player are valid.
    - If valid, the game's processing logic continues.
    - If invalid, help message is displayed to the player.
    """
    pattern = r'^[0-9()\+\-\*\/]*$'
    match_set = re.search(pattern, players_calc)
    if match_set is None:
        messages.add_message(
            request,
            messages.INFO,
            "Only arithmetic operators, digits, and rounded brackets are permitted characters."
        )
        return False
    return True


def check_legal_chars_seq(request, players_calc: str) -> bool:
    """
    Checks for known illegal character sequences entered by the player.
    - If valid, the game's processing logic continues.
    - If invalid, help message is displayed to the player.
    """
    patterns = ['+)', '-)', '*)', '/)']
    for pattern in patterns:
        if pattern in players_calc:
            messages.add_message(
                request,
                messages.INFO,
                f"The string sequence of {pattern} is an invalid one. " +
                "Please check the calculation string and resubmit."
            )
            return False
    return True


def check_brackets(request, players_calc: str) -> bool:
    """
    Checks that there is a matching amount of opening and closing
    brackets within the player's calculation.
    """
    if players_calc.count('(') != players_calc.count(')'):
        messages.add_message(
            request,
            messages.INFO,
            "There is a mismatch in the number of opening and closing brackets used."
        )
        return False
    return True


def strip_spaces(request, players_calc: str) -> str:
    """
    Removes unncessary spaces within the answer provided by the player.
    """
    return players_calc.replace(' ', '')


def calc_entered_is_valid(request, players_calc) -> bool:
    """ Validates that the calculation entered by the player is in a
    valid format.
    """
    players_calc = strip_spaces(request, players_calc)
    has_valid_chars = check_chars(request, players_calc)
    has_valid_brackets = check_brackets(request, players_calc)
    has_valid_sequences = check_legal_chars_seq(request, players_calc)
    if all([has_valid_chars, has_valid_brackets, has_valid_sequences]):
        return True
    messages.add_message(request, messages.INFO, message=f"\n{players_calc}",
                         extra_tags=f"Your Calculation Entered: {players_calc}")
    return False


def get_permissible_nums(request) -> list:
    """
    Returns a list of numbers that can be used to form a valid
    calculation for the game.
    """
    game_nums = request.GET.get('numbers_chosen')
    game_nums = ast.literal_eval(game_nums)
    return game_nums


def get_nums_used(request, players_calc: str) -> list:
    """
    Returns a list of numbers that have been used to form
    the player's calculation for the game.
    """
    nums_used = re.split(r'; |, |\*|\/|\+|\-|\(|\)', players_calc)
    nums_used[:] = (int(item) for item in nums_used if item != '')
    return nums_used


def is_calc_valid(request) -> bool:
    """
    Validates that the numbers used to form the player's calculation are
    permissible numbers for the game.
    """
    players_calc = request.GET.get('players_calculation')
    players_calc = strip_spaces(request, players_calc)
    nums_used = get_nums_used(request, players_calc)
    permissible_nums = get_permissible_nums(request)
    for test_num in nums_used:
        if test_num not in permissible_nums:
            return False
        permissible_nums.remove(test_num)
    return True
