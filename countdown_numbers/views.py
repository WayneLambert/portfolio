from random import choices, randint
from urllib.parse import urlencode
import re
import ast
from django.shortcuts import redirect, render
from django.urls import reverse
# pylint: disable=eval-used

from countdown_numbers.forms import NumberSelectionForm, SelectedNumbersForm

MAX_GAME_NUMBERS = 6

def get_numbers_chosen(num_from_top: int) -> list:
    NUMS_FROM_TOP = [25, 50, 75, 100]
    NUMS_FROM_BOTTOM = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

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


def game_screen(request):
    if request.method == 'POST':
        form = SelectedNumbersForm(request.POST)
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


def get_permissible_nums(request) -> list:
    game_nums = request.GET.get('numbers_chosen')
    game_nums = ast.literal_eval(game_nums)
    return game_nums


def get_nums_used(request, players_calc) -> list:
    nums_used = re.split(r'; |, |\*|\/|\+|\-|\(|\)', players_calc)
    nums_used[:] = (int(item) for item in nums_used if item != '')
    return nums_used


def is_calc_valid(request) ->bool:
    players_calc = request.GET.get('players_calculation')
    nums_used = get_nums_used(request, players_calc)
    permissible_nums = get_permissible_nums(request)
    for test_num in nums_used:
        if test_num not in permissible_nums:
            return False
        permissible_nums.remove(test_num)
    return True


def get_players_answer(request) ->int:
    players_calc = request.GET.get('players_calculation')
    players_answer = eval(players_calc)
    return players_answer


def get_closest_answer(request) ->int:
    return 100


def results_screen(request):
    valid_calc = is_calc_valid(request)
    if valid_calc:
        players_answer = get_players_answer(request)
    closest_answer = get_closest_answer(request)

    context = {
        'valid_calc': valid_calc,
        'players_answer': players_answer,
        'closest_answer': closest_answer,
    }

    return render(request, 'countdown_numbers/results.html', context)
