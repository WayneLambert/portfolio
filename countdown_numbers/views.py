from random import choices, randint
from urllib.parse import urlencode
from django.shortcuts import redirect, render
from django.urls import reverse

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

# TEMP BLOCK:
test_numbers_chosen = get_numbers_chosen(3)
# END TEMP BLOCK:

def get_target_number():
    return randint(100, 999)

def build_game_url(form):
    num_from_top = form.cleaned_data.get('num_from_top')
    numbers_chosen = get_numbers_chosen(num_from_top=num_from_top)
    target_number = get_target_number()
    base_url = reverse('countdown-numbers:game')
    numbers_chosen_url = urlencode({'numbers_chosen': numbers_chosen})
    target_number_url = urlencode({'target_number': target_number})
    full_url = f'{base_url}?{numbers_chosen_url}&{target_number_url}'
    return full_url

def selection_screen(request):
    form = NumberSelectionForm()
    if request.method == 'POST':
        form = NumberSelectionForm(request.POST)
        if form.is_valid():
            url = build_game_url(form)
            return redirect(url)
    else:
        form = NumberSelectionForm()

    return render(request, 'countdown_numbers/selection.html', {'form': form})


def game_screen(request):
    form = SelectedNumbersForm()

    if request.method == 'POST':
        form = SelectedNumbersForm(request.POST)
        if form.is_valid():
            base_url = reverse('countdown-numbers:results')

            numbers_chosen = request.META['HTTP_REFERER'][-MAX_GAME_NUMBERS:]
            numbers_chosen_url = urlencode({'numbers_chosen': numbers_chosen})

            players_calculation = form.cleaned_data.get('players_calculation')
            players_calculation_url = urlencode(
                {'players_calculation': players_calculation})

            full_url = f'{base_url}?{numbers_chosen_url}&{players_calculation_url}'
            return redirect(full_url)

    context = {
        'form': form,
    }

    return render(request, 'countdown_numbers/game.html', context)


# def results_screen(request):
#     numbers_chosen = request.GET['numbers_chosen']


#     context = {
#         'numbers_chosen': numbers_chosen,
#     }

#     return render(request, 'countdown_numbers/results.html', context)
