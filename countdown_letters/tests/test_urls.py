from django.urls import resolve, reverse


def test_selection_screen():
    """ Verify that the `selection` url invokes intended view """
    resolver = resolve(reverse('countdown_letters:selection'))
    assert resolver.view_name, 'selection_screen'

def test_game_screen():
    """ Verify that the `game` url invokes intended view """
    resolver = resolve(reverse('countdown_letters:game'))
    assert resolver.view_name, 'game_screen'

def test_results_screen():
    """ Verify that the `results` url invokes intended view """
    resolver = resolve(reverse('countdown_letters:results'))
    assert resolver.view_name, 'results_screen'
