""" Tests the website's external links (defined as teplate tags)

These test that the links are still returning a 200 status code and are
therefore not leading the site visitor to a 404 page.

Unfortunately, the links to either the LinkedIn profile page or to any
of the product pages on Amazon cannot be verified as having a `200`
status code.

LinkedIn returns a status code of `999` and Amazon's product pages
returns a `503`. In both cases, this is for any request that would
otherwise either result in a `200` or a `404` status.

This could perhaps be overcome by signing up to the respective APIs.

999 Error Code explanation:
https://www.deadlinkchecker.com/error-codes.asp

Methods are labelled as @staticmethod since the template tags does not
require an argument called `self`. Links are placed into categories for
organisational purposes and to facilitate testing.
"""

import os

import pytest
import requests

from apps.pages.templatetags.ext_links import (
    Contacts,
    CountdownLetters,
    CountdownNumbers,
    DataScience,
    LinkGenerator,
    Scraping,
    SocialMedia,
    TextAnalysis,
)

from .helpers import app_names


@pytest.mark.slow(reason="Sends a GET request to each link")
class TestSocialMedia:
    @staticmethod
    def test_github_profile():
        link = requests.get(SocialMedia.github_profile_link())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_github_portfolio():
        link = requests.get(SocialMedia.github_portfolio_link())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_github_portfolio_issues_link():
        link = requests.get(SocialMedia.github_portfolio_issues_link())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_stack_overflow_profile():
        link = requests.get(SocialMedia.stack_overflow_profile_link())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_google_maps_location():
        link = requests.get(SocialMedia.google_maps_location_link())
        assert link.status_code == 200, "Should return an `OK` status"


@pytest.mark.slow(reason="Sends a GET request to each link")
@pytest.mark.parametrize(argnames="type", argvalues=["code", "issues"])
@pytest.mark.parametrize(argnames="app", argvalues=app_names())
class TestLinkGenerator:
    @staticmethod
    def test_github_url(type, app):
        link = requests.get(LinkGenerator.github_url(type, app))
        assert link.status_code == 200, "Should return an `OK` status"


@pytest.mark.slow(reason="Sends a GET request")
class TestContacts:
    @staticmethod
    def test_google_maps_embed_link():
        link = requests.get(Contacts.google_maps_embed_link())
        assert link.status_code == 200, "Should return an `OK` status"
        assert b"B15 3PA" in link.content, "Should contain the postcode of B15 3PA"


@pytest.mark.skipif("GITHUB_RUN_ID" in os.environ, reason="Times out in GitHub Actions")
@pytest.mark.slow(reason="Sends a GET request to each link")
class TestCountdownLetters:
    @staticmethod
    def test_game_rules():
        link = requests.get(CountdownLetters.game_rules(), timeout=10)
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_views_source_code():
        link = requests.get(CountdownLetters.views_source_code())
        assert link.status_code == 200, "Should return an `OK` status"


@pytest.mark.slow(reason="Sends a GET request to each link")
class TestCountdownNumbers:
    @staticmethod
    def test_views_source_code():
        link = requests.get(CountdownNumbers.views_source_code())
        assert link.status_code == 200, "Should return an `OK` status"


@pytest.mark.slow(reason="Sends a GET request to each link")
class TestScraping:
    @staticmethod
    def test_churchill_speech():
        link = requests.get(Scraping.churchill_speech())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_gettysburg_speech():
        link = requests.get(Scraping.gettysburg_speech())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_gettysburg_source_code():
        link = requests.get(Scraping.gettysburg_source_code())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_churchill_source_code():
        link = requests.get(Scraping.churchill_source_code())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_referendum_source_code():
        link = requests.get(Scraping.referendum_source_code())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_sample_referendum_results():
        link = requests.get(Scraping.sample_referendum_results())
        assert link.status_code == 200, "Should return an `OK` status"


@pytest.mark.slow(reason="Sends a GET request")
class TestTextAnalysis:
    @staticmethod
    def test_views_source_code():
        link = requests.get(TextAnalysis.views_source_code())
        assert link.status_code == 200, "Should return an `OK` status"


@pytest.mark.slow(reason="Sends a GET request to each link")
class TestDataScience:
    @staticmethod
    def test_notebooks():
        link = requests.get(DataScience.notebooks())
        assert link.status_code == 200, "Should return an `OK` status"

    @staticmethod
    def test_github_issues():
        link = requests.get(DataScience.github_issues())
        assert link.status_code == 200, "Should return an `OK` status"
