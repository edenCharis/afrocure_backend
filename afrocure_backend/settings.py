# afrocure_backend/settings.py

import os
from pathlib import Path

import dj_database_url

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env") 


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY","p6v$3!2z#e&9@r1q8s7*4t0f%y+u!o@l")

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
     'cloudinary',
    'cloudinary_storage',
    # Local apps
    'products',
    'cart',
    'orders',
    'accounts',
]

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # En premier !
    'django.middleware.security.SecurityMiddleware',
    # ... reste du middleware
]


DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        engine='django.db.backends.postgresql'
    )
}
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # Vite dev server
    "https://afrocure.onrender.com",  # Production frontend
]


# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # required
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # required
    'django.contrib.messages.middleware.MessageMiddleware',     # required
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # your custom templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ALLOWED_HOSTS = ['.onrender.com']
DEBUG = False

# JWT + DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}