import os
import dj_database_url
from decouple import config
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# from django.conf.global_settings import DATABASES

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "config('SECRET_KEY')"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['855a0716958c.ngrok.io']

# Application definition

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # libraries and frameworks
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',

    # django-rest-auth
    'rest_auth',

    # reset password
    'django_rest_passwordreset',

    # django filters
    'django_filters',

    # apps
    'users.apps.UsersConfig',
    'accountant.apps.AccountantConfig',
    'news.apps.NewsConfig',
    'reports.apps.ReportsConfig',

    # cors
    'corsheaders',
    'Vlad',
]

SITE_ID = 1

AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.backends.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'EXCEPTION_HANDLER': 'users.exceptions.user_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',

    # django-filters setup
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
    },
    'LOGIN_URL': '/admin/login/?next=/admin/',
    'LOGOUT_URL': '/admin/logout/',
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# APPEND_SLASH = False
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:3001',
    'http://localhost:8000',
]

ROOT_URLCONF = 'unnamed_project.urls'

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

WSGI_APPLICATION = 'unnamed_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DEPLOY = config('DEPLOY', cast=bool)
# if DEPLOY:
#     DATABASES = {
#         'default': dj_database_url.config(default=config('DATABASE_URL'))
#     }
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': config('DB_NAME'),
#             'USER': config('DB_USER'),
#             'PASSWORD': config('DB_PASS'),
#             'HOST': config('DB_HOST'),
#             'PORT': config('DB_PORT')
#         }
#     }


DATABASES_URL = 'postgres://rqgehybrogueht:dc2330968da00894c68ee3b186f4e5532cf2727285ff007b5c35663fe267da83@ec2-54-167-152-185.compute-1.amazonaws.com:5432/d230gc92pkm9hs'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lolik',
        'USER': 'kana3',
        'PASSWORD': '123333',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# django_heroku.settings(locals())


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'alex.web.developer.kg@gmail.com'  # config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = 'ffzrsonqhiwrmoha'  # config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
