from urllib.parse import urlencode

from django.urls import reverse

from . import logic


def build_game_screen_url(form) -> str:
    """
    Builds the game screen's URL based upon the game's logic for
    choosing the letters for the game.
    """
    num_vowels_selected = form.cleaned_data.get('num_vowels_selected')
    letters_chosen = logic.get_letters_chosen(num_vowels=num_vowels_selected)
    base_url = reverse('countdown_letters:game')
    letters_chosen_url = urlencode({'letters_chosen': letters_chosen})

    return f"{base_url}?{letters_chosen_url}"


def build_results_screen_url(request, form) -> str:
    """
    Builds the results screen's URL based upon the game's chosen letters
    and the player's selected word.
    """
    base_url = reverse('countdown_letters:results')

    letters_chosen = request.META['HTTP_REFERER'][-logic.GameSetup.MAX_GAME_LETTERS:]
    letters_chosen_url = urlencode({'letters_chosen': letters_chosen})

    players_word = form.cleaned_data.get('players_word').upper()
    players_word_url = urlencode({'players_word': players_word})

    return f"{base_url}?{letters_chosen_url}&{players_word_url}"
