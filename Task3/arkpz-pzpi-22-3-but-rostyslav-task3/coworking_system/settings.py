import os
from pathlib import Path
from datetime import timedelta

# Шлях до папки проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),  # Було, наприклад, 5 хв
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}

# Секретний ключ для безпеки (зміни для комерційного використання)
SECRET_KEY = 'django-insecure-c02+tta+#b2*r&%#^dldd8kt=$-%&psp$un^*usz=y4a^c!t83'

# Режим розробки (вимкни для продакшену)
DEBUG = True

# Дозволені хости
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Встановлені додатки
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # Для авторизації (MF1)
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Для REST API
    'drf_yasg',  # Для Swagger
    'api',  # Наш додаток
    'rest_framework_simplejwt',
]

# Проміжне ПЗ
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Основний файл маршрутів
ROOT_URLCONF = 'coworking_system.urls'

# Налаштування шаблонів
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI-додаток
WSGI_APPLICATION = 'coworking_system.wsgi.application'

# База даних (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Авторизація (MF1)
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Налаштування REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Налаштування Swagger для підтримки Bearer JWT токена
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header using the Bearer scheme. Example: "Authorization: Bearer <token>"',
        }
    }
}

# Локалізація
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'Europe/Kyiv'
USE_I18N = True
USE_TZ = True

# Статичні файли
STATIC_URL = 'static/'

# Тип автоінкрементного поля
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Налаштування безпеки для комерційного використання
SECURE_SSL_REDIRECT = False  # Увімкни True для HTTPS
CSRF_COOKIE_SECURE = False  # Увімкни True для HTTPS
SESSION_COOKIE_SECURE = False  # Увімкни True для HTTPS

