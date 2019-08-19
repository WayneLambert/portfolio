from random import choices, random
from urllib.parse import urlencode
from django.shortcuts import redirect, render
from django.urls import reverse

from countdown.forms import LetterSelectionForm, SelectedLettersForm

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
            base_url = reverse('game')
            letters_chosen_url = urlencode({'letters_chosen': letters_chosen})
            full_url = f'{base_url}?{letters_chosen_url}'
            return redirect(full_url)
    else:
        form = LetterSelectionForm()

    return render(request, 'countdown/selection.html', {'form': form})


def game_screen(request):
    form = SelectedLettersForm()

    if request.method == 'POST':
        form = SelectedLettersForm(request.POST)
        if form.is_valid():
            base_url = reverse('results')

            letters_chosen = request.META['HTTP_REFERER'][-MAX_GAME_LETTERS:]
            letters_chosen_url = urlencode({'letters_chosen': letters_chosen})

            players_word = form.cleaned_data.get('players_word')
            players_word_url = urlencode({'players_word': players_word})

            # susies_word_url = ...
            # longest_possible_word = get_longest_possible_word(letters_chosen)
            # longest_possible_word_url = urlencode(
            #     {'longest_possible_word': longest_possible_word})

            full_url = f'{base_url}?{letters_chosen_url}?{players_word_url}'
            return redirect(full_url)
        else:
            form = SelectedLettersForm()

    context = {
        'form': form,
    }

    return render(request, 'countdown/game.html', context)


words_list = []
with open('countdown/words.txt', 'r') as words_file:
    for word in words_file:
        words_list.append(word.strip('\n'))

words_list = tuple(words_list)


# FIXME: letters_chosen was orignally a hard-coded list. This needs to be passed on
def get_longest_possible_word(words: tuple, letters_chosen: str) -> str:
    """ Returns the longest word in words.txt from the selected letters. """
    cumulative_max_letter_count = 0
    for tested_word in words:
        letters_in_selection = list(letters_chosen)
        letters_in_tested_word = list(tested_word)
        if len(letters_in_tested_word) < len(letters_in_selection):
            common_letters = set(letters_in_selection).intersection(
                letters_in_tested_word)
            letter_count = len(common_letters)
            if letter_count > cumulative_max_letter_count:
                cumulative_max_letter_count = letter_count
                longest_possible_word = tested_word
    return longest_possible_word


def is_valid_word(answer: str) -> bool:
    """ Is deemed a valid word if it belongs to the words.txt file """
    if answer.lower() in words_list:
        return True


def is_eligible_answer(answer: str) -> bool:
    """
    Returns whether the answer given is an eligible one
    (i.e. it uses only available letters)
    """
    letters_in_selection = list(letters_selection)
    letters_in_answer = list(answer)
    while letters_in_answer:
        for letter in answer:
            if letter in letters_in_answer and letter in letters_in_selection:
                letters_in_selection.remove(letter)
                letters_in_answer.remove(letter)
            else:
                return False
        return True


def get_answer_length(answer: str) -> int:
    """ If answer is valid, returns the length of the answer given by the player. """
    if is_eligible_answer(answer) and is_valid_word(answer):
        return len(answer)


def results_screen(request):

    # Check player's anser is valid in the words.txt file
    # Check player's answer is eligible
    # Create context which gives the answer length
    # Create context variable that gives the player's score
    # Compute Susie's answer to the word puzzle
    # Create context variable for Susie's answer
    # Create context variable for Susie's number_of_letters_used
    # Create context variable for Susie's score

    # comp_answer = get_longest_possible_word(words_list)

    context = {}

    return render(request, 'countdown/results.html', context)
