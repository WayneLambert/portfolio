from django.views.generic import ListView, TemplateView

from blog.models import Post


class HomeView(ListView):
    """ Custom view sets default behaviour for all list views to subclass
        and inherit for their own implementation """
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    queryset = Post.objects.prefetch_related('categories').select_related('author__user')[:3]


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class ReadingListView(TemplateView):
    template_name = 'reading_list.html'


class AboutMeView(TemplateView):
    template_name = 'about_me.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy.html'


# Skills
class BackEndSkillsView(TemplateView):
    template_name = 'skills/back_end.html'


class FrontEndSkillsView(TemplateView):
    template_name = 'skills/front_end.html'


class InfrastructureSkillsView(TemplateView):
    template_name = 'skills/infrastructure.html'


class SoftwareSkillsView(TemplateView):
    template_name = 'skills/software.html'


# Reviews
class BlogReviewView(TemplateView):
    template_name = 'reviews/blog.html'
