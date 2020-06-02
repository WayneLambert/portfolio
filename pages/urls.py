from django.urls import path

from .views import (BlogPostExampleView, ContactView, CVView,
                    HomeView, PortfolioView, WorkSearchProjectView)

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('cv', CVView.as_view(), name='cv'),
    path('contact', ContactView.as_view(), name='contact'),
    path('work-search', WorkSearchProjectView.as_view(), name='work_search'),
    path('blog-post-example', BlogPostExampleView.as_view(), name='blog_post_example'),
]
