"""
Django settings for simR project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m121fuicgj5gd-4a1g@6jkitxbc%inpycqi8*8n*s#%^s6s$!2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'simr-backend.onrender.com']


# Application definition

INSTALLED_APPS = [

    'corsheaders',
    'data.apps.DataConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",  # new

    'allauth',
    'allauth.account',
    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',

]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'simR.middleware.SyncToAsyncMiddleware',

    "allauth.account.middleware.AccountMiddleware",#allauth regisration

    'corsheaders.middleware.CorsMiddleware',

]

CORS_ALLOW_ALL_ORIGINS = True   

ROOT_URLCONF = 'simR.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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


SOCIALACCOUNT_PROVIDERS = {
    # For each OAuth based provider, either add a ``SocialApp``
    # (``socialaccount`` app) containing the required client
    # credentials, or list them here:
    'google': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': '',
        },
    },
    'facebook': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': '',
        },
    },
}

WSGI_APPLICATION = 'simR.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         "NAME": "dj_test",
#         "USER": "postgres",
#         "PASSWORD": "1234",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
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

TIME_ZONE = 'CET'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIR = [
    BASE_DIR/'static'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

# Change the default class of user 
AUTH_USER_MODEL = 'data.CustomUser'

# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'lezhang.pia@gmail.com'
EMAIL_HOST_PASSWORD = 'kbjl lwsx nbwt irrq'

#django-allauth registraion settings 
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_RATE_LIMITS = {
    "change_password": "5/m/user", # Changing the password (for already authenticated users).
    "manage_email": "10/m/user", # Email management related actions, such as add, remove, change primary.
    "reset_password":"20/m/ip,5/m/key", # Requesting a password reset. The email for which the password is to be reset is passed as the key.
    "reauthenticate":"10/m/user", # Reauthentication (for users already logged in).
    "reset_password_from_key":"20/m/ip", # Password reset (the view the password reset email links to).
    "signup":"20/m/ip", # Signups.
    "login":"30/m/ip", # Logins.
    "login_failed":"10/m/ip,5/5m/key",
    # Restricts the allowed number of failed login attempts. When exceeded, the user is prohibited from logging in for the remainder of the rate limit. Important: while this protects the allauth login view, it does not protect Django’s admin login from being brute forced. Note that a successful login will clear this rate limit.
    "confirm_email":"1/3m/key",
    # Users can request email confirmation mails via the email management view, and, implicitly, when logging in with an unverified account. This rate limit prevents users from sending too many of these mails.
}

SITE_ID = 1 
ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # new
#or any other page  
ACCOUNT_LOGOUT_REDIRECT_URL ='/accounts/login/' 

ASYNC_SUPPORT = True
