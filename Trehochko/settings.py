from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG"))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig'
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

ROOT_URLCONF = 'Trehochko.urls'

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

WSGI_APPLICATION = 'Trehochko.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Talent
if int(os.getenv("PRODUCTION")) == 1:
    TALENT_CLIENT_ID = 'J0kI8tJuJXVPdHmuprtg90OCHaDnschInCB0AnrHqyV8wPcn'
    TALENT_CLIENT_SECRET = 'sKxWlUmfx31SKjANOKzI0z25OlSIVUYwL6AdmxBgQbactpC3'
elif int(os.getenv("PRODUCTION")) == 2:
    TALENT_CLIENT_ID = 'D4Ujfa5d7xvp1xNKfkn60NMtHqERuk6K5FYqBXIGRrVsiJlA'
    TALENT_CLIENT_SECRET = '93PkO8SLEpTxfxYVAX8ghsHJR5eNRds5UnhXSADKZWtqJoKK'
else:
    TALENT_CLIENT_ID = 'DfRppyk69WQwy8MqEXvN8QH00XnbL53lVNTh3aJO4MeUy4i8'
    TALENT_CLIENT_SECRET = 'lETSQxfXM4Jo123NSKD1Pd7SCJfXdPZiUXKMg9WL5pgKkA9Y'

TALENT_AUTHORIZATION_ENDPOINT = 'https://talent.kruzhok.org/oauth/authorize/'
TALENT_TOKEN_ENDPOINT = 'https://talent.kruzhok.org/api/oauth/issue-token/'


# Steam
OPEN_ID_NS = 'http://specs.openid.net/auth/2.0'
OPEN_ID_CLAIMED_ID = 'http://specs.openid.net/auth/2.0/identifier_select'
OPEN_ID_IDENTITY = 'http://specs.openid.net/auth/2.0/identifier_select'
FORMAT_STEAM_AUTH_URL = 'https://steamcommunity.com/openid/login?{}'

# Blizzard
AUTHLIB_OAUTH_CLIENTS = {
    'blizzard': {
        'client_id': 'caefd4ae9ecd47dba636010127390a56',
        'client_secret': 'hyorRZmiZxUHc2wwGePF5lglUpTB1wp3',
    }
}
BLIZZARD_CONF_URL = 'https://eu.battle.net/oauth/.well-known/openid-configuration'
BLIZZARD_API_TOKEN_URL = 'https://eu.battle.net/oauth/token'
BLIZZARD_API_AUTHORIZE_URL = 'https://eu.battle.net/oauth/authorize'
BLIZZARD_API_USERINFO_URL = 'https://eu.battle.net/oauth/userinfo'
