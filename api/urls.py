from django.urls import include, path
from blog.views_api import PostListAPI_View, PostDetailAPI_View


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('blog/', PostListAPI_View.as_view()),
    path('blog/<int:pk>/', PostDetailAPI_View.as_view()),
]
