from django.shortcuts import redirect, render

from apps.countdown_letters import logic, utils, validations
from apps.countdown_letters.forms import LetterSelectionForm, SelectedLettersForm


def selection_screen(request):
    form = LetterSelectionForm()
    if request.method == 'POST':
        form = LetterSelectionForm(request.POST)
        if form.is_valid():
            num_vowels_selected = form.cleaned_data.get('num_vowels_selected')
            full_url = utils.build_game_screen_url(num_vowels_selected)
            return redirect(full_url)
    else:
        form = LetterSelectionForm()

    context = {'form': form}

    return render(request, 'countdown_letters/selection.html', context)


def game_screen(request):
    form = SelectedLettersForm()

    if request.method == 'POST':
        form = SelectedLettersForm(request.POST)
        if form.is_valid():
            players_word = form.cleaned_data.get('players_word').upper()
            letters_chosen = request.META['HTTP_REFERER'][-logic.GameSetup.MAX_GAME_LETTERS:]
            full_url = utils.build_results_screen_url(letters_chosen, players_word)
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

    if shortlisted_words := logic.get_shortlisted_words(
        logic.get_words(), letters_chosen
    ):
        comp_word = logic.get_longest_possible_word(shortlisted_words)
        winning_word = comp_word if len(comp_word) > player_word_len else players_word
        definition_data = logic.lookup_definition_data(winning_word)
    else:
        players_word, comp_word, winning_word = 'N/A', 'N/A', 'N/A'
        eligible_answer = False
        definition_data = {
            'definition': 'N/A',
            'word_class': 'N/A'
        }

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
