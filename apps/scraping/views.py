from django.views.generic import TemplateView


class ScrapingOptionsView(TemplateView):
    template_name = "scraping_options.html"
