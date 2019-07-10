from django.urls import include, path
from blog.views_api import (PostListAPI_View,
                            PostDetailAPI_View,
                            CategoryListAPI_View
                            )


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('blog/posts/', PostListAPI_View.as_view()),
    path('blog/posts/<int:pk>/', PostDetailAPI_View.as_view()),
    path('blog/categories/', CategoryListAPI_View.as_view()),
]
