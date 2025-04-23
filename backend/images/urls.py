from rest_framework.routers import DefaultRouter
from .views import ImageEntryViewSet

router = DefaultRouter()
router.register('images', ImageEntryViewSet, basename='images')
urlpatterns = router.urls
