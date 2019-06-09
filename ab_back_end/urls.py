from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from ab_back_end import views
from scraping import churchill_speech, gettysburg_speech
from scraping import views as scraping_views
from wordcount import views as wordcount_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    # path('api/', include('api.urls')),

    # The URLs for the Wordcount app
    path('check-wordcount/', wordcount_views.check_wordcount, name='check-wordcount'),
    path('count/', wordcount_views.count, name='count'),

    # The URLs for the Scraping app
    path('speech-list/', scraping_views.speech_list, name='speech-list'),
    path('churchill-speech/', churchill_speech.get_churchill_speech,
         name='churchill-speech'),
    path('gettysburg-speech/', gettysburg_speech.get_gettysburg_speech,
         name='gettysburg-speech'),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
