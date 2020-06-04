from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path

from ab_back_end.settings import ADMIN_ALIAS
from blog.sitemap import CategorySitemap, PostSitemap
from contacts import views as contacts_views

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path('djga/', include('google_analytics.urls')),
    path('', include('pages.urls', namespace='pages')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contact/', include('contacts.urls', namespace='contacts')),
    path('contact-submitted/', contacts_views.contact_submitted, 'contact-submitted'),
    path('users/', include('users.urls', namespace='users')),
    path('countdown-letters/', include('countdown_letters.urls', namespace='countdown_letters')),
    path('countdown-numbers/', include('countdown_numbers.urls', namespace='countdown_numbers')),
    path('text_analysis/', include('text_analysis.urls', namespace='text_analysis')),
    path('roulette/', include('roulette.urls', namespace='roulette')),
    path('scraping/', include('scraping.urls', namespace='scraping')),
    path('api/', include('api.urls', namespace='api')),
]

sitemaps = {
    'categories': CategorySitemap,
    'posts': PostSitemap,
}

# Admin Site and Password Reset Functionality
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
urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
