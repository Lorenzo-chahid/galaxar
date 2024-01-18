import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

# Chemin de base de votre projet Django
BASE_DIR = Path(__file__).resolve().parent.parent


# Fonction pour obtenir les variables d'environnement
def get_env_variable(var_name, default=None):
    try:
        return os.environ[var_name]
    except KeyError:
        if default is None:
            error_msg = f"Set the {var_name} environment variable"
            raise ImproperlyConfigured(error_msg)
        else:
            return default


# Sécurité
SECRET_KEY = get_env_variable(
    "DJANGO_SECRET_KEY",
    "django-insecure-0im_p_hnq4@0nm+ck2l_&@)7lr0$b08&$dx35*4$xh4-x27(-*",
)
DEBUG = get_env_variable("DJANGO_DEBUG", "False") != "False"
ALLOWED_HOSTS = ["your-app-name.herokuapp.com", "localhost", "127.0.0.1"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "events",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Gestion des fichiers statiques
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Gestion des CORS
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mycalendar.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "frontend" / "build"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "mycalendar.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# Remplacez ce qui précède par la configuration de votre base de données pour la production

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    # ... vos validateurs de mot de passe
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = "fr-fr"
TIME_ZONE = "Europe/Brussels"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "build" / "static",
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Configuration des CORS
CORS_ALLOW_ALL_ORIGINS = True

# Configuration par défaut pour l'auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"