import ast
import re

from django.contrib import messages


def check_chars(request, players_calc: str) -> bool:
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


def check_brackets(request, players_calc: str) -> bool:
    if players_calc.count('(') != players_calc.count(')'):
        messages.add_message(
            request,
            messages.INFO,
            "There is a mismatch in the number of opening and closing brackets used."
        )
        return False
    return True


def strip_spaces(request, players_calc: str) -> str:
    if ' ' in players_calc:
        return players_calc.replace(' ', '')
    return players_calc


def calc_entered_is_valid(request, players_calc) -> bool:
    players_calc = strip_spaces(request, players_calc)
    has_valid_chars = check_chars(request, players_calc)
    has_valid_brackets = check_brackets(request, players_calc)
    if all([has_valid_chars, has_valid_brackets]):
        return True
    else:
        messages.add_message(request, messages.INFO, message=f"\n{players_calc}",
                             extra_tags=f"Your Calculation Entered: {players_calc}")
        return False


def get_permissible_nums(request) -> list:
    game_nums = request.GET.get('numbers_chosen')
    game_nums = ast.literal_eval(game_nums)
    return game_nums


def get_nums_used(request, players_calc: str) -> list:
    nums_used = re.split(r'; |, |\*|\/|\+|\-|\(|\)', players_calc)
    nums_used[:] = (int(item) for item in nums_used if item != '')
    return nums_used


def is_calc_valid(request)-> bool:
    players_calc = request.GET.get('players_calculation')
    players_calc = strip_spaces(request, players_calc)
    nums_used = get_nums_used(request, players_calc)
    permissible_nums = get_permissible_nums(request)
    for test_num in nums_used:
        if test_num not in permissible_nums:
            return False
        permissible_nums.remove(test_num)
    return True
