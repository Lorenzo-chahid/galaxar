"""
WSGI config for mycalendar project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

import django
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mycalendar.settings")
django.setup()

# Exécuter les migrations
call_command("migrate")
call_command("collectstatic", interactive=False, verbosity=0)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mycalendar.settings")

application = get_wsgi_application()
