"""
Django settings for ft_transcendence project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os #used for env variables

from pathlib import Path
from datetime import timedelta	# for JWT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',			# Django admin tools
	'django.contrib.auth',			# User authentications
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'corsheaders',					# Adds Cross-Origin Resource Sharing (CORS) headers to responses

	'authentication',				# Our authentication application for the login/regist/logout
	'users',						# our users application

	'gunicorn',						# wsgi server
	'rest_framework',
	'rest_framework_simplejwt',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'authentication.middleware.JwtAuthMiddleware',
]

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework_simplejwt.authentication.JWTAuthentication',
	),
}

ROOT_URLCONF = 'ft_transcendence.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'ft_transcendence.wsgi.application'
ASGI_APPLICATION = 'ft_transcendence.asgi.application'

# Set https
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.getenv("DB_NAME"),
		'USER': os.getenv("DB_USER"),
		'PASSWORD': os.getenv("DB_PASSWORD"),
		'HOST': os.getenv("DB_HOST"),
		'PORT': os.getenv("DB_PORT"),
	}
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_ROOT = '/shared_media/'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Added for user authentication
AUTH_USER_MODEL = 'users.SiteUser'  # Tells Django to use our own user model

ALLOWED_HOSTS = [
	'localhost',
	'127.0.0.1',
]

CORS_ALLOWED_ORIGINS = [
	'https://localhost:8000',
	'https://localhost:5555'
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
	'https://localhost',
	'https://localhost:5555',
]


SIMPLE_JWT = {
	'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
	'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
	'ROTATE_REFRESH_TOKENS': False,
	'BLACKLIST_AFTER_ROTATION': True,
	'ALGORITHM': 'HS256',
	'SIGNING_KEY':  os.environ.get('JWT_KEY',),
	'AUTH_HEADER_TYPES': ('Bearer',),
	'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
}