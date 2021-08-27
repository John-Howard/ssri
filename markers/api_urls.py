"""Markers API URL Configuration."""

from rest_framework import routers

from markers.api_views import MarkerViewSet

router = routers.DefaultRouter()
router.register(r"markers", MarkerViewSet)

urlpatterns = router.urls
