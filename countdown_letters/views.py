from urllib.parse import urlencode

from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LetterSelectionForm, SelectedLettersForm
from .logic import (GameSetup, get_game_score, get_letters_chosen,
                    get_longest_possible_word, get_result, get_shortlisted_words,
                    get_words, lookup_definition, present_definition)
from .validations import is_eligible_answer, is_in_oxford_api


def selection_screen(request):
    form = LetterSelectionForm()
    if request.method == 'POST':
        form = LetterSelectionForm(request.POST)
        if form.is_valid():
            num_vowels_selected = form.cleaned_data.get('num_vowels_selected')
            letters_chosen = get_letters_chosen(num_vowels=num_vowels_selected)
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

            letters_chosen = request.META['HTTP_REFERER'][-GameSetup.MAX_GAME_LETTERS:]
            letters_chosen_url = urlencode({'letters_chosen': letters_chosen})

            players_word = form.cleaned_data.get('players_word').upper()
            players_word_url = urlencode({'players_word': players_word})

            full_url = f"{base_url}?{letters_chosen_url}&{players_word_url}"
            return redirect(full_url)

    context = {'form': form}

    return render(request, 'countdown_letters/game.html', context)


def results_screen(request):
    letters_chosen = request.GET['letters_chosen']
    listed_words = get_words()

    players_word = request.GET['players_word']
    valid_word = is_in_oxford_api(players_word)
    eligible_answer = is_eligible_answer(players_word, letters_chosen)
    if valid_word and eligible_answer:
        player_word_len = len(players_word)
        player_score = get_game_score(player_word_len)
    else:
        player_word_len, player_score = 0, 0

    shortlisted_words = get_shortlisted_words(listed_words, letters_chosen)
    comp_word = get_longest_possible_word(shortlisted_words)
    comp_word_len = len(comp_word)
    comp_score = get_game_score(comp_word_len)
    winning_word = comp_word if comp_word_len > player_word_len else players_word
    definition_result = lookup_definition(winning_word)
    definition = present_definition(definition_result)
    result = get_result(players_word, comp_word)

    context = {
        'letters_chosen': letters_chosen,
        'players_word': players_word,
        'eligible_answer': eligible_answer,
        'player_word_len': player_word_len,
        'player_score': player_score,
        'comp_word': comp_word,
        'comp_word_len': comp_word_len,
        'comp_score': comp_score,
        'winning_word': winning_word,
        'definition_result': definition_result,
        'definition': definition,
        'result': result,
    }

    return render(request, 'countdown_letters/results.html', context)
