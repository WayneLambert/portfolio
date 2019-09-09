import os
from random import choices, random
from urllib.parse import urlencode
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
import requests

from countdown_letters.forms import LetterSelectionForm, SelectedLettersForm

# Oxford Dictionaries API Credentials
OD_API_BASE_URL = os.environ['OD_API_BASE_URL']
OD_APPLICATION_ID = os.environ['OD_APPLICATION_ID']
OD_APPLICATION_KEY_1 = os.environ['OD_APPLICATION_KEY_1']

MAX_GAME_LETTERS = 9

def get_letters_chosen(num_vowels: int) -> str:
    WEIGHTED_VOWELS = list(
        'AAAAAAAAAAAAAAAEEEEEEEEEEEEEEEEEEEEEIIIIIIIIIIIIIOOOOOOOOOOOOOUUUUU')
    WEIGHTED_CONSONANTS = list(
        'BBCCCDDDDDDFFGGGHHJKLLLLLMMMMNNNNNNNNPPPPQRRRRRRRRRSSSSSSSSSTTTTTTTTTVWXYZ')
    num_consonants = MAX_GAME_LETTERS - num_vowels

    letters_chosen = []

    for _vowel in range(num_vowels):
        vowel_picked = choices(WEIGHTED_VOWELS)
        WEIGHTED_VOWELS.remove(vowel_picked[0])
        letters_chosen.append(vowel_picked)

    for _consonant in range(num_consonants):
        consonant_picked = choices(WEIGHTED_CONSONANTS)
        WEIGHTED_CONSONANTS.remove(consonant_picked[0])
        letters_chosen.append(consonant_picked)

    letters_chosen = sorted(letters_chosen, key=lambda k: random())
    letters_param = ''.join([
        item for ind_letter_list in letters_chosen for item in ind_letter_list])
    return letters_param


def selection_screen(request):
    form = LetterSelectionForm()
    if request.method == 'POST':
        form = LetterSelectionForm(request.POST)
        if form.is_valid():
            num_vowels_selected = form.cleaned_data.get('num_vowels_selected')
            letters_chosen = get_letters_chosen(num_vowels=num_vowels_selected)
            base_url = reverse('countdown-letters:game')
            letters_chosen_url = urlencode({'letters_chosen': letters_chosen})
            full_url = f'{base_url}?{letters_chosen_url}'
            return redirect(full_url)
    else:
        form = LetterSelectionForm()

    return render(request, 'countdown_letters/selection.html', {'form': form})


def game_screen(request):
    form = SelectedLettersForm()

    if request.method == 'POST':
        form = SelectedLettersForm(request.POST)
        if form.is_valid():
            base_url = reverse('countdown-letters:results')

            letters_chosen = request.META['HTTP_REFERER'][-MAX_GAME_LETTERS:]
            letters_chosen_url = urlencode({'letters_chosen': letters_chosen})

            players_word = form.cleaned_data.get('players_word')
            players_word_url = urlencode({'players_word': players_word})

            full_url = f'{base_url}?{letters_chosen_url}&{players_word_url}'
            return redirect(full_url)

    context = {
        'form': form,
    }

    return render(request, 'countdown_letters/game.html', context)


def get_words():
    words_list = []
    words_filename = os.path.join(settings.BASE_DIR, 'countdown_letters/words.txt')
    with open(words_filename, 'r') as words_file:
        for word in words_file:
            words_list.append(word.strip('\n'))

    words = tuple(words_list)
    return words


def get_longest_possible_word(words: tuple, letters: str) -> str:
    """ Returns the longest word in words.txt from the selected letters. """
    cumulative_max_letter_count = 0
    letters_in_selection = list(letters)
    for tested_word in words:
        letters_in_tested_word = list(tested_word.upper())
        if len(letters_in_tested_word) < len(letters_in_selection):
            common_letters = set(letters_in_selection).intersection(
                letters_in_tested_word)
            letter_count = len(common_letters)
            if letter_count > cumulative_max_letter_count:
                if len(tested_word) == len(common_letters):
                    cumulative_max_letter_count = letter_count
                    longest_possible_word = tested_word
    return longest_possible_word.upper()


def is_valid_word(answer: str) -> bool:
    words_list = get_words()
    if answer.lower() in words_list:
        return True


def is_eligible_answer(answer: str, letters: str) -> bool:
    letters_in_answer = list(answer)
    letters_in_selection = list(letters)
    while letters_in_answer:
        for letter in answer:
            if letter in letters_in_answer and letter in letters_in_selection:
                letters_in_selection.remove(letter)
                letters_in_answer.remove(letter)
            else:
                return False
        return True


def get_game_score(word_len: int) -> int:
    if word_len == 9:
        return word_len ** 2
    else:
        return word_len

def lookup_definition(request, word_to_lookup: str) -> dict:
    """ Retrieve dictionary definition of winning word using 'Oxford Dictionaries' API """
    LANGUAGE = 'en-gb'
    url = f'{OD_API_BASE_URL}{LANGUAGE}{"/"}{word_to_lookup.lower()}'
    headers = {
        "app_id": OD_APPLICATION_ID,
        "app_key": OD_APPLICATION_KEY_1,
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        definition_found = False
        definition = ''
        word_class = ''
    else:
        definition_found = True
        response_json = response.json()
        definition = response_json['results'][0]['lexicalEntries'][0]
        word_class = definition['lexicalCategory']['text']
        try:
            definition = definition['entries'][0]['senses'][0]['definitions'][0].capitalize()
        except KeyError:
            definition = f"""The definition for {word_to_lookup} cannot be found
                             in the Oxford Dictionary API."""

    definition_result = {
        'definition_found': definition_found,
        'definition': definition,
        'word_class': word_class,
    }

    return definition_result


def get_result(player_word: str, comp_word: str) -> str:
    if len(player_word) > len(comp_word):
        return 'Player wins'
    if len(player_word) < len(comp_word):
        return 'Susie wins'
    else:
        return 'Draw'


def results_screen(request):
    letters_chosen = request.GET['letters_chosen']
    listed_words = get_words()

    players_word = request.GET['players_word']
    valid_word = is_valid_word(players_word)
    eligible_answer = is_eligible_answer(players_word, letters_chosen)
    if valid_word and eligible_answer:
        player_word_len = len(players_word)
        player_score = get_game_score(player_word_len)
    else:
        player_word_len = 0
        player_score = 0

    comp_word = get_longest_possible_word(listed_words, letters_chosen)
    comp_word_len = len(comp_word)
    comp_score = get_game_score(comp_word_len)
    winning_word = comp_word if comp_word_len > player_word_len else players_word
    definition = lookup_definition(request, winning_word)
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
        'definition': definition,
        'result': result,
    }

    return render(request, 'countdown_letters/results.html', context)
