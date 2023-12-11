""" Functions required to implement the game's core logic. """

# pylint: disable=eval-used
import itertools
import operator

from collections import defaultdict, deque
from random import choices, randint
from typing import DefaultDict, Dict, List

from django.urls import reverse
from django.utils.http import urlencode


def get_numbers_chosen(num_from_top: int) -> List:
    """
    Returns an appropriate proportion of numbers from the top and bottom
    row within the randomised game selection according to their
    frequency of existence
    """

    MAX_GAME_NUMBERS: int = 6
    NUMS_FROM_TOP = [25, 50, 75, 100]
    NUMS_FROM_BOTTOM = list(range(1, 11)) * 2

    num_from_bottom: int = MAX_GAME_NUMBERS - num_from_top

    numbers_chosen = []

    for _ in range(num_from_top):
        num_from_top_picked = choices(NUMS_FROM_TOP)[0]
        NUMS_FROM_TOP.remove(num_from_top_picked)
        numbers_chosen.append(num_from_top_picked)

    for _ in range(num_from_bottom):
        num_from_bottom_picked = choices(NUMS_FROM_BOTTOM)[0]
        NUMS_FROM_BOTTOM.remove(num_from_bottom_picked)
        numbers_chosen.append(num_from_bottom_picked)

    return numbers_chosen


def get_target_number() -> int:
    """Generates a random number between 100 and 999"""
    return randint(100, 999)


def build_game_url(num_from_top: int) -> str:
    """Generates the URL for the `game` screen"""
    base_url = reverse("countdown_numbers:game")
    target_number_url = urlencode({"target_number": get_target_number()})
    numbers_chosen_url = urlencode(
        {"numbers_chosen": get_numbers_chosen(num_from_top=num_from_top)}
    )
    return f"{base_url}?{target_number_url}&{numbers_chosen_url}"


def get_game_nums(number_chosen: list) -> List:
    """Performs cleanup to get the game numbers as a list"""
    return number_chosen.strip("[").strip("]").replace(" ", "").split(",")


def get_player_num_achieved(players_calc: str) -> int:
    """Calculates number calculated according to the input answer"""
    return int(eval(players_calc))


def get_game_calcs(game_nums: list, stop_on=None) -> DefaultDict:
    """Calculates the possible calculations to the game"""
    operator_symbols = {
        "+": operator.add,
        "-": operator.sub,
        chr(215): operator.mul,
        chr(247): operator.truediv,
    }

    game_nums_permutations = itertools.permutations(game_nums)
    operator_combinations = itertools.product(operator_symbols.keys(), repeat=5)
    possibilities = itertools.product(game_nums_permutations, operator_combinations)

    game_calcs = defaultdict(list)
    calc_string = "(((({0} {6} {1}) {7} {2}) {8} {3}) {9} {4}) {10} {5}"
    for game_nums, operators in possibilities:
        calc = calc_string.format(*(game_nums + operators))

        value_queue = deque(game_nums)
        operators_queue = deque(operators)

        answer = value_queue.popleft()
        while value_queue:
            operator_function = operator_symbols[operators_queue.popleft()]
            next_value = value_queue.popleft()
            answer = operator_function(answer, next_value)
            if answer < 0 or answer != int(answer):
                break
        else:
            game_calcs[answer].append(calc)
            if answer == stop_on:
                break

    return game_calcs


def get_best_solution(game_nums: List, target: int) -> str:
    """Calculates a solution closest to the game's target number"""
    game_calcs = get_game_calcs(game_nums, stop_on=target)

    if target in game_calcs:
        return game_calcs[target][0]
    for num in range(1, 11):
        if target + num in game_calcs:
            return game_calcs[target + num][0]
        return game_calcs[target - num][0]
    return "No solution could be found"


def get_score_awarded(target_number: int, num_achieved: int) -> int:
    """
    Calculates the game score awarded based on the achieved
    calculation's proximity to the target number
    """
    if num_achieved == target_number:
        return 10
    elif target_number - 5 <= num_achieved <= target_number + 5:
        return 7
    elif target_number - 10 <= num_achieved <= target_number + 10:
        return 5
    else:
        return 0


def get_game_result(target: int, answers: Dict) -> str:
    """Returns the game's result as a string for template rendering"""
    comp_ans_variance = abs(answers["comp_num_achieved"] - target)
    player_ans_variance = abs(answers["player_num_achieved"] - target)
    if comp_ans_variance == player_ans_variance:
        return "Draw"
    else:
        return (
            "Player wins"
            if player_ans_variance < comp_ans_variance
            else "Rachel wins"
        )
