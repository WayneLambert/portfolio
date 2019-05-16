from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls
