from django.views.generic import ListView, TemplateView

from blog.models import Post


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    queryset = Post.objects.all().order_by('-publish_date')[:3]
    context_object_name = 'posts'

class PortfolioView(TemplateView):
    template_name = "portfolio.html"


class CVView(TemplateView):
    template_name = "cv.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class BlogPostExampleView(TemplateView):
    template_name = "blog_post.html"
