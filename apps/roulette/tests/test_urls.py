from django.urls import resolve, reverse


def test_game_screen():
    """Verify that the `game` url invokes intended view"""
    resolver = resolve(reverse("roulette:game"))
    assert resolver.view_name, "game"


def test_destination_screen():
    """Verify that the `destination` url invokes intended view"""
    resolver = resolve(reverse("roulette:destination"))
    assert resolver.view_name, "destination"


def test_results_screen():
    """Verify that the `destination-log-file` url invokes intended view"""
    resolver = resolve(reverse("roulette:log_file"))
    assert resolver.view_name, "log_file"
