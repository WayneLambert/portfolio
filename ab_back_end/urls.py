from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ab_back_end import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cv', views.view_cv, name='cv'),
    path('about-blog', views.about_blog, name='about-blog'),
    path('contact', views.contact_form, name='contact-form'),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('scraping/', include('scraping.urls')),
    path('wordcount/', include('wordcount.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
