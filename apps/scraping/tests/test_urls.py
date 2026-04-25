from django.urls import resolve, reverse


def test_scraping_options_screen():
    """Verify that the `scraping-options` url invokes intended view"""
    resolver = resolve(reverse("scraping:scraping_options"))
    assert resolver.view_name, "scraping_options"


def test_eu_referendum_results_screen():
    """Verify that the `eu-referendum-results` url invokes intended view"""
    resolver = resolve(reverse("scraping:referendum"))
    assert resolver.view_name, "referendum"
