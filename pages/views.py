from django.views.generic import TemplateView

from blog.views import PostView


class HomeView(PostView):
    template_name = 'home.html'

    def get_queryset(self):
        return self.queryset[:3]

class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class DevSkillsView(TemplateView):
    template_name = 'skills/back_end.html'


class ReadingListView(TemplateView):
    template_name = 'reading_list.html'


class AboutMeView(TemplateView):
    template_name = 'about_me.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy.html'


# Reviews
class BlogReviewView(TemplateView):
    template_name = 'reviews/blog.html'
