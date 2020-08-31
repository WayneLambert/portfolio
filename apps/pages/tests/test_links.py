""" Tests for the external links within the website.

These test that the links are still returning a 200 status code and are
therefore not leading the site visitor to a 404 page.

Unfortunately, the links to either the LinkedIn profile page or to any
of the product pages on Amazon cannot be verified as having a `200`
status code.

LinkedIn returns a status code of `999` and Amazon's product pages
returns a `503`. In both cases, this is for any request that would
otherwise either result in a `200` or a `404` status.

This could perhaps be overcome by signing up to the respective APIs.

999 Error Code explanation: https://www.deadlinkchecker.com/error-codes.asp
"""

import pytest
import requests

from apps.pages.templatetags.ext_links import Link


@pytest.mark.slow(reason='Sends a GET request to each link')
class TestLink:

    class TestSocialMedia:
        def test_github_profile(self):
            link = requests.get(Link.SocialMedia.github_profile_link())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_portfolio(self):
            link = requests.get(Link.SocialMedia.github_portfolio_link())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_portfolio_issues_link(self):
            link = requests.get(Link.SocialMedia.github_portfolio_issues_link())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_stack_overflow_profile(self):
            link = requests.get(Link.SocialMedia.stack_overflow_profile_link())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_google_maps_location(self):
            link = requests.get(Link.SocialMedia.google_maps_location_link())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestAPI:
        def test_source_code(self):
            link = requests.get(Link.API.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.API.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestBlog:
        def test_source_code(self):
            link = requests.get(Link.Blog.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.Blog.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestContacts:
        def test_source_code(self):
            link = requests.get(Link.Contacts.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.Contacts.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'

        def google_maps_embed_link(self):
            link = requests.get(Link.Contacts.google_maps_embed_link())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestCountdownLetters:
        def test_source_code(self):
            link = requests.get(Link.CountdownLetters.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.CountdownLetters.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_game_rules(self):
            link = requests.get(Link.CountdownLetters.game_rules())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_views_source_code(self):
            link = requests.get(Link.CountdownLetters.views_source_code())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestCountdownNumbers:
        def test_source_code(self):
            link = requests.get(Link.CountdownNumbers.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.CountdownNumbers.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_game_rules(self):
            link = requests.get(Link.CountdownNumbers.game_rules())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_views_source_code(self):
            link = requests.get(Link.CountdownNumbers.views_source_code())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestCV:
        def test_source_code(self):
            link = requests.get(Link.CV.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.CV.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestPages:
        def test_source_code(self):
            link = requests.get(Link.Pages.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.Pages.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestRoulette:
        def test_source_code(self):
            link = requests.get(Link.Roulette.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.Roulette.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestScraping:
        def test_source_code(self):
            link = requests.get(Link.Scraping.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.Scraping.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_churchill_speech(self):
            link = requests.get(Link.Scraping.churchill_speech())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_gettysburg_speech(self):
            link = requests.get(Link.Scraping.gettysburg_speech())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_gettysburg_source_code(self):
            link = requests.get(Link.Scraping.gettysburg_source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_churchill_source_code(self):
            link = requests.get(Link.Scraping.churchill_source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_referendum_source_code(self):
            link = requests.get(Link.Scraping.referendum_source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_sample_referendum_results(self):
            link = requests.get(Link.Scraping.sample_referendum_results())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestTextAnalysis:
        def test_source_code(self):
            link = requests.get(Link.TextAnalysis.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.TextAnalysis.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_views_source_code(self):
            link = requests.get(Link.TextAnalysis.views_source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

    class TestUsers:
        def test_source_code(self):
            link = requests.get(Link.Users.source_code())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.Users.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'


    class TestDataScience:
        def test_notebooks(self):
            link = requests.get(Link.DataScience.notebooks())
            assert link.status_code == 200, 'Should return an `OK` status'

        def test_github_issues(self):
            link = requests.get(Link.DataScience.github_issues())
            assert link.status_code == 200, 'Should return an `OK` status'
