# pylint: disable=eval-used

from urllib.parse import urlencode

from django.shortcuts import redirect, render
from django.urls import reverse

from apps.countdown_numbers import logic, utils, validations
from apps.countdown_numbers.forms import NumberSelectionForm, SelectedNumbersForm


def selection_screen(request):
    if request.method == 'POST':
        form = NumberSelectionForm(request.POST)
        if form.is_valid():
            num_from_top = form.cleaned_data.get('num_from_top')
            game_screen_url = logic.build_game_url(num_from_top)
            return redirect(game_screen_url)
    else:
        form = NumberSelectionForm()

    return render(request, 'countdown_numbers/selection.html', {'form': form})


def game_screen(request):
    if request.method == 'POST':
        form = SelectedNumbersForm(request.POST)
        calc_entered = form['players_calculation'].data
        is_valid_calc = validations.calc_entered_is_valid(request, calc_entered)
        if not is_valid_calc:
            return redirect(request.META['HTTP_REFERER'])
        if form.is_valid():
            base_url = reverse('countdown_numbers:results')
            referer_url = request.META['HTTP_REFERER'].split('?')[-1]

            players_calc_url = urlencode(
                {'players_calculation': form.cleaned_data.get('players_calculation')})

            results_screen_url = f"{base_url}?{referer_url}&{players_calc_url}"
            return redirect(results_screen_url)
    else:
        numbers_chosen = request.GET['numbers_chosen']
        context = {
            'form': SelectedNumbersForm(),
            'game_nums': logic.get_game_nums(numbers_chosen)
        }

        return render(request, 'countdown_numbers/game.html', context)


def results_screen(request):
    players_calc = request.GET.get('players_calculation')
    valid_calc = validations.is_calc_valid(request, players_calc)
    player_num_achieved = logic.get_player_num_achieved(players_calc)
    target_number = int(request.GET.get('target_number'))
    player_score, comp_score = 0, 0
    if valid_calc:
        player_score = logic.get_score_awarded(target_number, player_num_achieved)

    game_nums = validations.get_permissible_nums(request)
    best_solution = logic.get_best_solution(game_nums, target_number)
    best_solution = best_solution.replace(chr(215), '*').replace(chr(247), '/')
    comp_num_achieved = int(eval(best_solution))
    solution_str = f"""
        {best_solution.replace(
            '*', chr(215)).replace('/', chr(247))} = {comp_num_achieved}""".strip()
    answers = {
        'player_num_achieved': player_num_achieved,
        'comp_num_achieved': comp_num_achieved,
    }
    game_result = logic.get_game_result(target_number, answers)

    if valid_calc and game_result != 'comp_num_achieved':
        player_score = logic.get_score_awarded(target_number, player_num_achieved)
    if game_result != 'player_num_achieved':
        comp_score = logic.get_score_awarded(target_number, comp_num_achieved)

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

    utils.create_record(context)

    return render(request, 'countdown_numbers/results.html', context)
