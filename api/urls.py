from django.urls import path, include

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('books/', include('books.urls')),
    path('blog/', include('blog.urls')),
    path('todos/', include('todos.urls')),
    path('articles/', include('articles.urls')),
    path('analytics/', include('analytics.urls')),
]
