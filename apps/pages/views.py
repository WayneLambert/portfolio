from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from blog.models import Post


class SiteHomeView(ListView):
    """
    Limits published posts dataset to three most recently updated posts
    for the site's home page.
    """

    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    queryset = Post.published.all()[:3]


class PortfolioView(TemplateView):
    template_name = "portfolio.html"


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
