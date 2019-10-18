from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from ab_back_end.settings import ADMIN_ALIAS
from ab_back_end.views import (about_me, home, privacy_policy,
                               react_blog, reading_list, view_cv)
from blog.sitemap import CategorySitemap, PostSitemap
from contacts import views as contacts_views

urlpatterns = [
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
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path('djga/', include('google_analytics.urls')),
    path('', home, name='home'),
    path('cv', view_cv, name='view-cv'),
    path('blog/', include('blog.urls')),
    re_path('react-blog/*', react_blog, name='react-blog'),
    path('contact/', include('contacts.urls')),
    path(
        'contact-submitted/',
        contacts_views.contact_submitted,
        name='contact-submitted'
    ),
    path('users/', include('users.urls')),
    path('countdown-letters/', include('countdown_letters.urls')),
    path('countdown-numbers/', include('countdown_numbers.urls')),
    path('text_analysis/', include('text_analysis.urls')),
    path('roulette/', include('roulette.urls')),
    path('scraping/', include('scraping.urls')),
    path('about-me/', about_me, name='about-me'),
    path('privacy-policy/', privacy_policy, name='privacy-policy'),
    path('reading-list/', reading_list, name='reading-list'),
    path('api/', include('api.urls')),
]

sitemaps = {
    'categories': CategorySitemap,
    'posts': PostSitemap,
}

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
