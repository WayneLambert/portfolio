from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from ab_back_end import views as ab_back_end_views
from contacts import views as contacts_views
from ab_back_end.settings import ADMIN_ALIAS


urlpatterns = [
    path(
        f'{ADMIN_ALIAS}/password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='admin_password_reset',
    ),
    path(
        f'{ADMIN_ALIAS}/password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path(f'{ADMIN_ALIAS}/', admin.site.urls),
    path('', ab_back_end_views.home, name='home'),
    path('cv', ab_back_end_views.view_cv, name='view-cv'),
    path('about-blog', ab_back_end_views.about_blog, name='about-blog'),
    path('blog/', include('blog.urls')),
    path('contact/', include('contacts.urls')),
    path('contact-submitted/',
         contacts_views.contact_submitted,
         name='contact-submitted'
         ),
    path('users/', include('users.urls')),
    path('scraping/', include('scraping.urls')),
    path('count/', include('count.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
