# pylint: disable=redefined-outer-name
from django.urls import reverse

import pytest


def test_analyse_screen(client):
    """Asserts a site visitor can GET the `analyse` screen"""
    path = reverse("text_analysis:analyse")
    response = client.get(path)
    assert response.status_code == 200, "Should return an `OK` status code"


def test_analysis_screen_with_clean_text(client, text_to_analyse):
    """Asserts a site visitor can GET the `analysis` screen"""
    path = reverse("text_analysis:analysis")
    response = client.get(path, {"fulltext": text_to_analyse})
    assert response.status_code == 200, "Should return an `OK` status code"


def test_analysis_screen_with_dirty_text(client, dirty_text):
    """Asserts a site visitor can GET the `analysis` screen"""
    path = reverse("text_analysis:analysis")
    response = client.get(path, {"fulltext": dirty_text})
    assert response.status_code == 200, "Should return an `OK` status code"
