from urllib.parse import urlencode

from django.shortcuts import redirect, render
from django.urls import reverse

from . import logic, validations
from .forms import LetterSelectionForm, SelectedLettersForm


def selection_screen(request):
    form = LetterSelectionForm()
    if request.method == 'POST':
        form = LetterSelectionForm(request.POST)
        if form.is_valid():
            num_vowels_selected = form.cleaned_data.get('num_vowels_selected')
            letters_chosen = logic.get_letters_chosen(num_vowels=num_vowels_selected)
            base_url = reverse('countdown_letters:game')
            letters_chosen_url = urlencode({'letters_chosen': letters_chosen})
            full_url = f"{base_url}?{letters_chosen_url}"
            return redirect(full_url)
    else:
        form = LetterSelectionForm()

    return render(request, 'countdown_letters/selection.html', {'form': form})


def game_screen(request):
    form = SelectedLettersForm()

    if request.method == 'POST':
        form = SelectedLettersForm(request.POST)
        if form.is_valid():
            base_url = reverse('countdown_letters:results')

            letters_chosen = request.META['HTTP_REFERER'][-logic.GameSetup.MAX_GAME_LETTERS:]
            letters_chosen_url = urlencode({'letters_chosen': letters_chosen})

            players_word = form.cleaned_data.get('players_word').upper()
            players_word_url = urlencode({'players_word': players_word})

            full_url = f"{base_url}?{letters_chosen_url}&{players_word_url}"
            return redirect(full_url)

    context = {'form': form}

    return render(request, 'countdown_letters/game.html', context)


def results_screen(request):
    letters_chosen: str = request.GET['letters_chosen']
    file_words = logic.get_words()

    players_word: str = request.GET['players_word']
    valid_word = validations.is_in_oxford_api(players_word)
    eligible_answer = validations.is_eligible_answer(players_word, letters_chosen)
    if valid_word and eligible_answer:
        player_word_len = len(players_word)
        player_score = logic.get_game_score(player_word_len)
    else:
        player_word_len, player_score = 0, 0

    shortlisted_words = logic.get_shortlisted_words(file_words, letters_chosen)
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

    return render(request, 'countdown_letters/results.html', context)
