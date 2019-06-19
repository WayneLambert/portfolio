from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ab_back_end import views as ab_back_end_views
from contacts import views as contacts_views


urlpatterns = [
    path('admin/', admin.site.urls),
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
    path('wordcount/', include('wordcount.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
