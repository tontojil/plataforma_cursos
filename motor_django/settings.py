"""
Django settings for motor_django project.
Proyecto: Plataforma de Cursos Online - Eva 2
"""

from pathlib import Path
from decouple import config

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# Llave secreta y debug salen del .env, no van escritos aqui
SECRET_KEY = config('SECRET_KEY')

# En evaluacion se usa False para mostrar el 404 personalizado
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'testserver']


# Aplicaciones del proyecto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'cursos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'motor_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'motor_django.wsgi.application'


# Base de datos MySQL con datos del .env
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('NAME'),
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
    }
}


# Validacion de contrasenas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Zona horaria e idioma
LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = False


# Archivos estaticos
STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Llave primaria por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
