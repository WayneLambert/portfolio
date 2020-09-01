""" A series of external links within the website.

These exist for testing purposes since external links are susceptible to
being broken if a project is re-organised.

Since hard-coded links are avoided within the HTML templates, if there
is an update to the external URL, this needs to be updated here. The
template tag will propagate the change through to the templates.
"""

from django import template

register = template.Library()


class SocialMedia:
    @register.simple_tag
    def github_profile_link():
        return "https://github.com/WayneLambert/"

    @register.simple_tag
    def github_portfolio_link():
        return "https://github.com/WayneLambert/portfolio/"

    @register.simple_tag
    def github_portfolio_issues_link():
        return "https://github.com/WayneLambert/portfolio/issues?q=is%3Aissue"

    @register.simple_tag
    def stack_overflow_profile_link():
        return "https://stackoverflow.com/users/11211077/wayne-lambert?tab=profile"

    @register.simple_tag
    def linkedin_profile_link():
        return "https://www.linkedin.com/in/waynealambert/"

    @register.simple_tag
    def google_maps_location_link():
        return "https://www.google.co.uk/maps/place/Edgbaston,+Birmingham"

    @register.simple_tag
    def email_me_link():
        return "mailto:contact@waynelambert.dev"


class LinkGenerator:
    """
    Creates either a GitHub source code URL or the query string URL
    for a list of filtered issues for the given app.
    """
    @staticmethod
    @register.simple_tag
    def github_url(type: str, app: str) -> str:
        base_url = "https://github.com/WayneLambert/portfolio/"
        if type == 'code':
            query_str = f"tree/master/apps/{app}"
        else:
            query_str = f"issues?q=is%3Aissue+label%3A%22app%3A+{app}%22"
        
        return base_url + query_str


class Contacts:
    @register.simple_tag(name='google_maps_embed_link')
    def google_maps_embed_link():
        return "https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d2430.353171772638!2d-1.9222173833795277!3d52.47274087980513!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sB15%203!5e0!3m2!1sen!2suk!4v1592585652608!5m2!1sen!2suk"


class CountdownLetters:
    @register.simple_tag(name='countdown_letters_game_rules_link')
    def game_rules():
        return "http://wiki.apterous.org/Letters_game"

    @register.simple_tag(name='countdown_letters_views_source_code_link')
    def views_source_code():
        return "https://github.com/WayneLambert/portfolio/blob/master/apps/countdown_letters/views.py"


class CountdownNumbers:
    @register.simple_tag(name='countdown_numbers_game_rules_link')
    def game_rules():
        return "http://datagenetics.com/blog/august32014/index.html"

    @register.simple_tag(name='countdown_numbers_views_source_code_link')
    def views_source_code():
        return "https://github.com/WayneLambert/portfolio/blob/master/apps/countdown_numbers/views.py"


class Scraping:
    @register.simple_tag(name='churchill_speech_link')
    def churchill_speech():
        return "https://www.goodreads.com/quotes/55276-i-have-nothing-to-offer-but-blood-toil-tears-and"

    @register.simple_tag(name='gettysburg_speech_link')
    def gettysburg_speech():
        return "https://www.goodreads.com/work/quotes/4694-the-illustrated-gettysburg-address"

    @register.simple_tag(name='scraping_gettysburg_source_code_link')
    def gettysburg_source_code():
        scraping_code_url = LinkGenerator.github_url(type='code', app='scraping')
        return f"{scraping_code_url}{'/gettysburg.py'}"

    @register.simple_tag(name='scraping_churchill_source_code_link')
    def churchill_source_code():
        scraping_code_url = LinkGenerator.github_url(type='code', app='scraping')
        return f"{scraping_code_url}{'/churchill.py'}"

    @register.simple_tag(name='scraping_referendum_source_code_link')
    def referendum_source_code():
        scraping_code_url = LinkGenerator.github_url(type='code', app='scraping')
        return f"{scraping_code_url}{'/referendum.py'}"

    @register.simple_tag(name='scraping_sample_ref_results_link')
    def sample_referendum_results():
        return "https://www.bbc.co.uk/news/politics/eu_referendum/results/local/a"


class TextAnalysis:
    @register.simple_tag(name='text_analysis_views_source_code_link')
    def views_source_code():
        scraping_code_url = LinkGenerator.github_url(type='code', app='text_analysis')
        return f"{scraping_code_url}{'/views.py'}"


class DataScience:
    @register.simple_tag(name='data_science_portfolio_notebooks')
    def notebooks():
        return "https://github.com/WayneLambert/data-science-portfolio/tree/master/notebooks"

    @register.simple_tag(name='data_science_github_issues_link')
    def github_issues():
        return "https://github.com/WayneLambert/portfolio/issues?q=is%3Aissue+label%3A%22data+science%22+is%3Aclosed"
