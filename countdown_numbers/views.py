import ast
import itertools
import operator
import re
from collections import defaultdict, deque
from random import choices, randint
from urllib.parse import urlencode

from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from countdown_numbers.forms import NumberSelectionForm, SelectedNumbersForm
# pylint: disable=eval-used


MAX_GAME_NUMBERS = 6

def get_numbers_chosen(num_from_top: int) -> list:
    NUMS_FROM_TOP = [25, 50, 75, 100]
    NUMS_FROM_BOTTOM = list(range(1, 11)) * 2

    num_from_bottom = MAX_GAME_NUMBERS - num_from_top

    numbers_chosen = []

    for _num in range(num_from_top):
        num_from_top_picked = choices(NUMS_FROM_TOP)[0]
        NUMS_FROM_TOP.remove(num_from_top_picked)
        numbers_chosen.append(num_from_top_picked)

    for _num in range(num_from_bottom):
        num_from_bottom_picked = choices(NUMS_FROM_BOTTOM)[0]
        NUMS_FROM_BOTTOM.remove(num_from_bottom_picked)
        numbers_chosen.append(num_from_bottom_picked)

    return numbers_chosen


def get_target_number():
    return randint(100, 999)


def build_game_url(form):
    num_from_top = form.cleaned_data.get('num_from_top')
    base_url = reverse('countdown-numbers:game')
    target_number_url = urlencode({'target_number': get_target_number()})
    numbers_chosen_url = urlencode(
        {'numbers_chosen': get_numbers_chosen(num_from_top=num_from_top)})
    full_url = f'{base_url}?{target_number_url}&{numbers_chosen_url}'
    return full_url


def selection_screen(request):
    if request.method == 'POST':
        form = NumberSelectionForm(request.POST)
        if form.is_valid():
            game_screen_url = build_game_url(form)
            return redirect(game_screen_url)
    else:
        form = NumberSelectionForm()

    return render(request, 'countdown_numbers/selection.html', {'form': form})


def check_chars(request, players_calc: str):
    pattern = r'^[0-9()\+\-\*\/]*$'
    match_set = re.search(pattern, players_calc)
    if match_set is None:
        messages.add_message(request, messages.INFO, f"""Only arithmetic operators,
            numbers, and rounded brackets permitted.""")
        return False
    else:
        return True


def check_brackets(request, players_calc: str) ->bool:
    if players_calc.count('(') != players_calc.count(')'):
        messages.add_message(request, messages.INFO, f"""Mismatch in the number
            of opening/closing brackets used.""")
        return False
    else:
        return True


def check_spaces(request, players_calc: str) ->bool:
    if ' ' in players_calc:
        messages.add_message(request, messages.INFO, f"""There are spaces used
            within your calculation.""")
        return False
    else:
        return True


def calc_entered_is_valid(request, players_calc) -> bool:
    has_valid_chars = check_chars(request, players_calc)
    has_valid_brackets = check_brackets(request, players_calc)
    has_no_spaces = check_spaces(request, players_calc)
    if all([has_valid_chars, has_valid_brackets, has_no_spaces]):
        return True
    else:
        messages.add_message(request, messages.INFO, message=f'\n{players_calc}',
                             extra_tags=players_calc)
        return False


def game_screen(request):
    if request.method == 'POST':
        form = SelectedNumbersForm(request.POST)
        calc_entered = form['players_calculation'].data
        is_valid_calc = calc_entered_is_valid(request, calc_entered)
        if not is_valid_calc:
            return redirect(request.META['HTTP_REFERER'])
        if form.is_valid():
            base_url = reverse('countdown-numbers:results')
            referer_url = request.META['HTTP_REFERER'].split('?')[-1]

            players_calc_url = urlencode(
                {'players_calculation': form.cleaned_data.get('players_calculation')})

            results_screen_url = f'{base_url}?{referer_url}&{players_calc_url}'
            return redirect(results_screen_url)
    else:
        form = SelectedNumbersForm()

    return render(request, 'countdown_numbers/game.html', {'form': form})


def get_permissible_nums(request)-> list:
    game_nums = request.GET.get('numbers_chosen')
    game_nums = ast.literal_eval(game_nums)
    return game_nums


def get_nums_used(request, players_calc)-> list:
    nums_used = re.split(r'; |, |\*|\/|\+|\-|\(|\)', players_calc)
    nums_used[:] = (int(item) for item in nums_used if item != '')
    return nums_used


def is_calc_valid(request)-> bool:
    players_calc = request.GET.get('players_calculation')
    nums_used = get_nums_used(request, players_calc)
    permissible_nums = get_permissible_nums(request)
    for test_num in nums_used:
        if test_num not in permissible_nums:
            return False
        permissible_nums.remove(test_num)
    return True


def get_player_num_achieved(request)-> int:
    players_calc = request.GET.get('players_calculation')
    player_num_achieved = int(eval(players_calc))
    return player_num_achieved

operator_symbols = {
    '+': operator.add,
    '-': operator.sub,
    chr(215): operator.mul,
    chr(247): operator.truediv,
}


def get_game_calcs(request, game_nums, stop_on=None):
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


def get_best_solution(request, game_nums, target):
    game_calcs = get_game_calcs(request, game_nums, stop_on=target)

    if int(target) in game_calcs:
        return game_calcs[int(target)][0]
    else:
        for num in range(1, 11):
            if int(target) + num in game_calcs:
                return game_calcs[int(target) + num][0]
            elif int(target) - num in game_calcs:
                return game_calcs[int(target) - num][0]
        return f'No solution could be found'


def get_score_awarded(request, target_number: int, num_achieved: int)-> int:
    if num_achieved == target_number:
        points_awarded = 10
    elif target_number - 5 <= num_achieved <= target_number + 5:
        points_awarded = 7
    elif target_number - 10 <= num_achieved <= target_number + 10:
        points_awarded = 5
    else:
        points_awarded = 0
    return points_awarded


def get_closest_answer(target_number: int, answers: dict) ->int:
    closest_num = min(answers.values(), key=lambda num: abs(num - target_number))
    return closest_num


def get_game_result(closest_num: int, answers: dict)-> str:
    winner = list(answers.keys())[list(answers.values()).index(closest_num)]
    return winner


def results_screen(request):
    valid_calc = is_calc_valid(request)
    player_num_achieved = get_player_num_achieved(request)
    target_number = int(request.GET.get('target_number'))
    if valid_calc:
        player_score = get_score_awarded(request, target_number, player_num_achieved)
    else:
        player_score = 0

    game_nums = get_permissible_nums(request)
    best_solution = get_best_solution(request, game_nums, target_number)
    best_solution = best_solution.replace(chr(215), '*').replace(chr(247), '/')
    comp_num_achieved = int(eval(best_solution))
    solution_str = f"""
        {best_solution.replace('*', chr(215)).replace('/', chr(247))} = {comp_num_achieved}"""
    if valid_calc:
        player_score = get_score_awarded(request, target_number, player_num_achieved)
    comp_score = get_score_awarded(request, target_number, comp_num_achieved)
    answers = {
        'player_num_achieved': player_num_achieved,
        'comp_num_achieved': comp_num_achieved,
    }
    closest_num = get_closest_answer(target_number, answers)
    game_result = get_game_result(closest_num, answers)

    context = {
        'game_nums': game_nums,
        'valid_calc': valid_calc,
        'target_number': target_number,
        'player_num_achieved': player_num_achieved,
        'comp_num_achieved': comp_num_achieved,
        'solution_str': solution_str,
        'player_score': player_score,
        'comp_score': comp_score,
        'game_result': game_result,
    }

    return render(request, 'countdown_numbers/results.html', context)
