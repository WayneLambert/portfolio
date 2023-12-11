from django.urls import resolve, reverse


def test_analyse_screen():
    """Verify that the `analyse` url invokes intended view"""
    resolver = resolve(reverse("text_analysis:analyse"))
    assert resolver.view_name, "analyse"


def test_analysis_screen():
    """Verify that the `analysis` url invokes intended view"""
    resolver = resolve(reverse("text_analysis:analysis"))
    assert resolver.view_name, "analysis"
