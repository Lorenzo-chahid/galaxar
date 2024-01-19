from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import EventViewSet
from django.urls import path, include, re_path
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r"events", EventViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    re_path(r"^.*", TemplateView.as_view(template_name="index.html")),
]
