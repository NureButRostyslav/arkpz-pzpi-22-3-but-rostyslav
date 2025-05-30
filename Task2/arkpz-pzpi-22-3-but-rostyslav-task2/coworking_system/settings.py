import os
from pathlib import Path

# Шлях до папки проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретний ключ для безпеки
SECRET_KEY = 'django-insecure-249ір9кн93к38ап9цкпис9а'

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
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
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
SECURE_SSL_REDIRECT = False  # True для HTTPS
CSRF_COOKIE_SECURE = False  # True для HTTPS
SESSION_COOKIE_SECURE = False  # True для HTTPS
