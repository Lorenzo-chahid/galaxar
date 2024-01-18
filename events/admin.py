from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "day", "start_time", "end_time", "category")
    search_fields = ("title", "category")
    list_filter = ("day", "category")


# Autres configurations spécifiques à EventAdmin si nécessaire
