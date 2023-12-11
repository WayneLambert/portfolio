from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from two_factor.urls import urlpatterns as tf_urls

from aa_project.settings.base import DJANGO_ADMIN_LOGIN_PATH

from blog.sitemap import CategorySitemap, PostSitemap
from pages.views import BadRequestView, PageNotFoundView, PermissionDeniedView


handler400 = BadRequestView.as_view()
handler403 = PermissionDeniedView.as_view()
handler404 = PageNotFoundView.as_view()
handler500 = "apps.pages.views.handler500"


urlpatterns = [
    path("tinymce/", include("tinymce.urls")),
    path("", include(tf_urls)),
    path("", include("pages.urls", namespace="pages")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("contact/", include("contacts.urls", namespace="contacts")),
    path("cv/", include("cv.urls", namespace="cv")),
    path("countdown-letters/", include("countdown_letters.urls", namespace="countdown_letters")),
    path("countdown-numbers/", include("countdown_numbers.urls", namespace="countdown_numbers")),
    path("text-analysis/", include("text_analysis.urls", namespace="text_analysis")),
    path("roulette/", include("roulette.urls", namespace="roulette")),
    path("scraping/", include("scraping.urls", namespace="scraping")),
    path("api/", include("api.urls", namespace="api")),
]


# Admin Site URLs
urlpatterns += [
    path(
        f"{DJANGO_ADMIN_LOGIN_PATH}/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path(
        f"{DJANGO_ADMIN_LOGIN_PATH}/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(f"{DJANGO_ADMIN_LOGIN_PATH}/", admin.site.urls),
]

# Sitemap Config
sitemaps = {
    "categories": CategorySitemap,
    "posts": PostSitemap,
}

urlpatterns += [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

# Django Debug Toolbar Config
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
