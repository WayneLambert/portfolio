from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.base import RedirectView

from apps.blog.models import Post


class SiteHomeView(ListView):
    """
    Limits published posts dataset to three most recently updated posts
    for the site's home page.
    """

    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    queryset = Post.published.all()[:3]


# Static Pages
class PortfolioView(TemplateView):
    template_name = "portfolio.html"


class ReadingListView(TemplateView):
    template_name = "reading_list.html"


class AboutMeView(TemplateView):
    template_name = "about_me.html"


class PrivacyPolicyView(TemplateView):
    template_name = "privacy.html"


# Skills
class SkillsView(RedirectView):
    permanent = True
    pattern_name = "pages:back_end_skills"


class BackEndSkillsView(TemplateView):
    template_name = "skills/back_end.html"


class FrontEndSkillsView(TemplateView):
    template_name = "skills/front_end.html"


class InfrastructureSkillsView(TemplateView):
    template_name = "skills/infrastructure.html"


class SoftwareSkillsView(TemplateView):
    template_name = "skills/software.html"


# Reviews
class BlogReviewView(TemplateView):
    template_name = "reviews/blog.html"


class APIReviewView(TemplateView):
    template_name = "reviews/api.html"


class CountdownLettersReviewView(TemplateView):
    template_name = "reviews/countdown_letters.html"


class CountdownNumbersReviewView(TemplateView):
    template_name = "reviews/countdown_numbers.html"


class RouletteReviewView(TemplateView):
    template_name = "reviews/roulette.html"


class ScrapingReviewView(TemplateView):
    template_name = "reviews/scraping.html"


class TextAnalysisReviewView(TemplateView):
    template_name = "reviews/text_analysis.html"


class DataScienceReviewView(TemplateView):
    template_name = "reviews/data_science.html"


# Custom Error Templates
class BadRequestView(TemplateView):
    template_name = "errors/400.html"


class PermissionDeniedView(TemplateView):
    template_name = "errors/403.html"


class PageNotFoundView(TemplateView):
    template_name = "errors/404.html"


def handler500(request):  # pragma: no cover
    response = render(request, template_name="errors/500.html", context={})
    response.status_code = 500
    return response
