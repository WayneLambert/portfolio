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
LANGUAGE = 'en-gb'
headers = {
    "app_id": OD_APPLICATION_ID,
    "app_key": OD_APPLICATION_KEY_1,
}

MAX_GAME_LETTERS = 9

def get_letters_chosen(num_vowels: int) -> str:
    """
    To give an appropriate proportion of the various vowels and consonants
    within the randomised game selections, there are:
    """

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
            base_url = reverse('countdown_letters:game')
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
            base_url = reverse('countdown_letters:results')

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


def get_words() ->tuple:
    words_list = []
    words_filename = os.path.join(settings.BASE_DIR, 'countdown_letters/words.txt')
    with open(words_filename, 'r') as words_file:
        for word in words_file:
            words_list.append(word.strip('\n'))

    words = tuple(words_list)
    return words


def get_shortlisted_words(words: tuple, letters: str) -> dict:
    """
    Returns a shortlist of the accumulatively gathered longest words
    in the running order of cycling through words.txt
    """
    shortlisted_words = {}
    cumulative_max_letter_count = 0
    letters_in_selection = list(letters)
    for tested_word in words:
        letters_in_tested_word = list(tested_word.upper())
        if len(letters_in_tested_word) < len(letters_in_selection):
            common_letters = set(letters_in_selection).intersection(
                letters_in_tested_word)
            letter_count = len(common_letters)
            if letter_count >= cumulative_max_letter_count:
                if len(tested_word) == len(common_letters):
                    cumulative_max_letter_count = letter_count
                    shortlisted_words[tested_word] = cumulative_max_letter_count
    return shortlisted_words


def is_in_oxford_api(word: str) ->bool:
    url = f'{OD_API_BASE_URL}{"lemmas/"}{LANGUAGE}{"/"}{word.lower()}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False


def get_longest_possible_word(shortlisted_words: dict) -> str:
    sorted_list = sorted(shortlisted_words.items(), reverse=True)
    for item in sorted_list:
        if is_in_oxford_api(item[0]):
            longest_possible_word = item[0]
            return longest_possible_word.upper()


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


def get_lemmas_response_json(word: str) ->dict:
    lemmas_url = f"{OD_API_BASE_URL}{'lemmas/'}{LANGUAGE}{'/'}{word.lower()}"
    lemmas_response = requests.get(lemmas_url, headers=headers)
    lemmas_response_json = lemmas_response.json()
    return lemmas_response_json


def get_alt_word(word: str) -> str:
    """
    Retrieve alternative word to the exact winning word. The singular form of the
    word may be the referenced word in the Oxford definitions API.
    """
    lemmas_json = get_lemmas_response_json(word)
    alt_word_lookup = lemmas_json['results'][0]['lexicalEntries'][0]
    alt_word_lookup = alt_word_lookup['inflectionOf'][0]['id']
    return alt_word_lookup


def lookup_definition(word: str) -> dict:
    """
    Retrieve dictionary definition of winning word using 'Oxford Dictionaries API'.
    An alternative form of the word is used if the Oxford API does not return a
    definition for the exact match of the winning form. In this case, it return a
    result from the lemmas query.
    """
    definitions_url = f'{OD_API_BASE_URL}{"entries/"}{LANGUAGE}{"/"}{word.lower()}'
    definitions_response = requests.get(definitions_url, headers=headers)
    if definitions_response.status_code == 200:
        definitions_response_json = definitions_response.json()
        definition = definitions_response_json['results'][0]['lexicalEntries'][0]
        word_class = definition['lexicalCategory']['text']
        try:
            definition = definition['entries'][0]['senses'][0]['definitions'][0].capitalize()
        except KeyError:
            definition = f"""The definition for '{word}' cannot be found
                             in the Oxford Dictionary API."""
        alt_word_lookup = word
    else:
        alt_word_lookup = get_alt_word(word)
        definition = lookup_definition(alt_word_lookup)
        lemmas_json = get_lemmas_response_json(word)
        word_class = lemmas_json['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']

    definition_result = {
        'alt_word_lookup': alt_word_lookup,
        'definition': definition,
        'word_class': word_class,
    }

    return definition_result


def present_definition(definition_result):
    if isinstance(definition_result['definition'], dict):
        return definition_result['definition']['definition']
    return definition_result['definition']


def get_result(player_word: str, comp_word: str) -> str:
    if len(player_word) > len(comp_word):
        return 'You win'
    if len(player_word) < len(comp_word):
        return 'Susie wins'
    else:
        return 'Draw'


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
        player_word_len = 0
        player_score = 0

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
