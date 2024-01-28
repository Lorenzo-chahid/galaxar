from rest_framework.routers import DefaultRouter
from .views import EventViewSet, home
from django.urls import path, include

router = DefaultRouter()
router.register(r"events", EventViewSet)

urlpatterns = [
    path("", home),
    path("router/", include(router.urls)),
]
