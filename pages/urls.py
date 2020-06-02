from django.urls import path

from .views import (BlogPostExampleView, ContactView, CVView, HomeView,
                    PortfolioView)

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('cv', CVView.as_view(), name='cv'),
    path('contact', ContactView.as_view(), name='contact'),
    path('blog-post-example', BlogPostExampleView.as_view(), name='blog_post_example'),
]
