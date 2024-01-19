from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver


def create_superuser():
    """Crée un superutilisateur si aucun superutilisateur n'existe."""
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser("admin", "admin@example.com", "password1991")


@receiver(post_migrate)
def add_superuser(sender, **kwargs):
    """Crée un superutilisateur après la migration."""
    create_superuser()


# Create your models here.
class Event(models.Model):
    CATEGORY_CHOICES = [
        ("science", "Science"),
        ("technology", "Technology"),
    ]

    title = models.CharField(
        "Title of the event", max_length=70, help_text="Title of the event"
    )
    day = models.DateField("Day of the event", help_text="Day of the event")
    start_time = models.TimeField("Starting time", help_text="Starting time")
    end_time = models.TimeField("Final time", help_text="Final time")
    end_day = models.DateField(
        "End day of the event", help_text="End day of the event", null=True, blank=True
    )
    notes = models.TextField(
        "Textual Notes", help_text="Textual Notes", blank=True, null=True
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def clean(self):
        # Validation pour s'assurer que end_day n'est pas antérieur à day
        if self.end_day < self.day:
            raise ValidationError("End day cannot be earlier than the start day.")

    class Meta:
        verbose_name = "Scheduling"
        verbose_name_plural = "Scheduling"

    # Autres méthodes et logiques
