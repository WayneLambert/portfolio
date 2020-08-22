from django.shortcuts import redirect, render

from apps.countdown_letters import logic, utils, validations
from apps.countdown_letters.forms import LetterSelectionForm, SelectedLettersForm


def selection_screen(request):
    form = LetterSelectionForm()
    if request.method == 'POST':
        form = LetterSelectionForm(request.POST)
        if form.is_valid():
            full_url = utils.build_game_screen_url(form)
            return redirect(full_url)
    else:
        form = LetterSelectionForm()

    return render(request, 'countdown_letters/selection.html', {'form': form})


def game_screen(request):
    form = SelectedLettersForm()

    if request.method == 'POST':
        form = SelectedLettersForm(request.POST)
        if form.is_valid():
            full_url = utils.build_results_screen_url(request, form)
            return redirect(full_url)

    context = {'form': form}

    return render(request, 'countdown_letters/game.html', context)


def results_screen(request):
    letters_chosen: str = request.GET['letters_chosen']

    players_word: str = request.GET['players_word']
    valid_word = validations.is_in_oxford_api(players_word)
    eligible_answer = validations.is_eligible_answer(players_word, letters_chosen)
    if valid_word and eligible_answer:
        player_word_len = len(players_word)
        player_score = logic.get_game_score(player_word_len)
    else:
        player_word_len, player_score = 0, 0

    shortlisted_words = logic.get_shortlisted_words(logic.get_words(), letters_chosen)
    comp_word = logic.get_longest_possible_word(shortlisted_words)
    if comp_word:
        winning_word = comp_word if len(comp_word) > player_word_len else players_word
        definition_data = logic.lookup_definition_data(winning_word)
    else:
        winning_word, definition_data = 'N/A', 'N/A'

    context = {
        'letters_chosen': letters_chosen,
        'players_word': players_word,
        'eligible_answer': eligible_answer,
        'player_word_len': player_word_len,
        'player_score': player_score,
        'comp_word': comp_word,
        'comp_word_len': len(comp_word) if comp_word else 0,
        'comp_score': logic.get_game_score(len(comp_word)) if comp_word else 0,
        'winning_word': comp_word if len(comp_word) > player_word_len else players_word,
        'definition_data': definition_data,
        'result': logic.get_result(players_word, comp_word),
    }

    utils.create_record(context)

    return render(request, 'countdown_letters/results.html', context)
