from django.urls import resolve, reverse


def test_scraping_options_screen():
    """Verify that the `scraping-options` url invokes intended view"""
    resolver = resolve(reverse("scraping:scraping_options"))
    assert resolver.view_name, "scraping_options"


def test_churchill_speech_screen():
    """Verify that the `churchill-speech` url invokes intended view"""
    resolver = resolve(reverse("scraping:churchill_speech"))
    assert resolver.view_name, "churchill_speech"


def test_gettysburg_speech_screen():
    """Verify that the `gettysburg-speech` url invokes intended view"""
    resolver = resolve(reverse("scraping:gettysburg_speech"))
    assert resolver.view_name, "gettysburg_speech"


def test_eu_referendum_results_screen():
    """Verify that the `eu-referendum-results` url invokes intended view"""
    resolver = resolve(reverse("scraping:referendum"))
    assert resolver.view_name, "referendum"
