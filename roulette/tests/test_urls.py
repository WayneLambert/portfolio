from django.urls import resolve, reverse


def test_game_screen():
    """ Verify that the `game` url invokes intended view """
    resolver = resolve(reverse('roulette:holiday_roulette'))
    assert resolver.view_name, 'holiday_roulette'

def test_destination_screen():
    """ Verify that the `destination` url invokes intended view """
    resolver = resolve(reverse('roulette:holiday_destination'))
    assert resolver.view_name, 'holiday_destination'

def test_results_screen():
    """ Verify that the `destination-log-file` url invokes intended view """
    resolver = resolve(reverse('roulette:destination_log_file'))
    assert resolver.view_name, 'destination_log_file'
