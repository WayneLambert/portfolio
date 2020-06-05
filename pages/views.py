from django.views.generic import ListView, TemplateView

from blog.models import Post


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    queryset = Post.get_posts()[:3]
    context_object_name = 'posts'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class ReadingListView(TemplateView):
    template_name = 'reading_list.html'


class AboutMeView(TemplateView):
    template_name = 'about_me.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'
