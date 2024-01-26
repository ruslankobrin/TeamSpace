from django.urls import path, include
from rest_framework.routers import DefaultRouter

from teamapp.views import PersonViewSet, TeamViewSet

router = DefaultRouter()
router.register(r"people", PersonViewSet, basename="person")
router.register(r"teams", TeamViewSet, basename="team")

urlpatterns = [
    path("api/", include(router.urls)),
]
