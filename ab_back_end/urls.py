""" Project level URLs

Includes config for the following:

- Custom error pages
- Through route URLs to third party packages
- Through route URLs to the project's app's repspective URL
  configurations
- Customised path to the Django admin area and admin password reset
  functionality
- Sitemap configuration
- Django Debug Toolbar configuration
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include
from django.urls import path
from django.urls import re_path

from blog.sitemap import CategorySitemap
from blog.sitemap import PostSitemap
from pages.views import SiteBadRequestView
from pages.views import SitePageNotFoundView
from pages.views import SitePermissionDeniedView

from .settings import ADMIN_ALIAS


handler400 = SiteBadRequestView.as_view()
handler403 = SitePermissionDeniedView.as_view()
handler404 = SitePageNotFoundView.as_view()
handler500 = 'pages.views.handler500'


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path('djga/', include('google_analytics.urls')),
    path('', include('pages.urls', namespace='pages')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', include('contacts.urls', namespace='contacts')),
    path('cv/', include('cv.urls', namespace='cv')),
    path('countdown-letters/', include(
        'countdown_letters.urls', namespace='countdown_letters')),
    path('countdown-numbers/', include(
        'countdown_numbers.urls', namespace='countdown_numbers')),
    path('text_analysis/', include(
        'text_analysis.urls', namespace='text_analysis')),
    path('roulette/', include('roulette.urls', namespace='roulette')),
    path('scraping/', include('scraping.urls', namespace='scraping')),
    path('api/', include('api.urls', namespace='api')),
]


# Admin Site URLs
urlpatterns += [
    path(
        f'{ADMIN_ALIAS}/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset'
    ),
    path(
        f'{ADMIN_ALIAS}/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
    path(f'{ADMIN_ALIAS}/', admin.site.urls),
]

# Sitemap Config
sitemaps = {
    'categories': CategorySitemap,
    'posts': PostSitemap,
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

# Django Debug Toolbar Config
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
