# pylint: disable=eval-used

import itertools
import operator
from collections import defaultdict, deque
from random import choices, randint

from django.urls import reverse
from django.utils.http import urlencode


def get_numbers_chosen(num_from_top: int) -> list:
    MAX_GAME_NUMBERS = 6
    NUMS_FROM_TOP = [25, 50, 75, 100]
    NUMS_FROM_BOTTOM = list(range(1, 11)) * 2

    num_from_bottom = MAX_GAME_NUMBERS - num_from_top

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
    return randint(100, 999)


def build_game_url(form) -> str:
    num_from_top = form.cleaned_data.get('num_from_top')
    base_url = reverse('countdown_numbers:game')
    target_number_url = urlencode({'target_number': get_target_number()})
    numbers_chosen_url = urlencode(
        {'numbers_chosen': get_numbers_chosen(num_from_top=num_from_top)})
    return f"{base_url}?{target_number_url}&{numbers_chosen_url}"


def get_game_nums(request) -> list:
    nums = request.GET['numbers_chosen'].strip('[').strip(']').replace(' ', '')
    return nums.split(',')


def get_player_num_achieved(request) -> int:
    players_calc = request.GET.get('players_calculation')
    return int(eval(players_calc))


def get_game_calcs(request, game_nums: list, stop_on=None) -> defaultdict:

    operator_symbols = {
        '+': operator.add,
        '-': operator.sub,
        chr(215): operator.mul,
        chr(247): operator.truediv,
    }

    game_nums_permutations = itertools.permutations(game_nums)
    operator_combinations = itertools.product(operator_symbols.keys(), repeat=5)
    possibilities = itertools.product(game_nums_permutations, operator_combinations)

    game_calcs = defaultdict(list)
    calc_string = u'(((({0} {6} {1}) {7} {2}) {8} {3}) {9} {4}) {10} {5}'
    for (game_nums, operators) in possibilities:
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


def get_best_solution(request, game_nums, target) -> str:
    game_calcs = get_game_calcs(request, game_nums, stop_on=target)

    if int(target) in game_calcs:
        return game_calcs[int(target)][0]
    else:
        for num in range(1, 11):
            if int(target) + num in game_calcs:
                return game_calcs[int(target) + num][0]
            elif int(target) - num in game_calcs:
                return game_calcs[int(target) - num][0]
        return "No solution could be found"


def get_score_awarded(request, target_number: int, num_achieved: int) -> int:
    if num_achieved == target_number:
        points_awarded = 10
    elif target_number - 5 <= num_achieved <= target_number + 5:
        points_awarded = 7
    elif target_number - 10 <= num_achieved <= target_number + 10:
        points_awarded = 5
    else:
        points_awarded = 0
    return points_awarded


def get_game_result(target: int, answers: dict)-> str:
    if answers['comp_num_achieved'] == answers['player_num_achieved']:
        result = 'Draw'
    else:
        result = min(answers.items(), key=lambda kv: abs(kv[1] - target))[0]
    return result