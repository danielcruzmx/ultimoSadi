"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(WSGI_DIR)
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)


ON_OPENSHIFT = False
DEBUG = True

if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

import sys
sys.path.append(os.path.join(REPO_DIR, 'libs'))
import secrets
SECRETS = secrets.getter(os.path.join(DATA_DIR, 'secrets.json'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRETS['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get('DEBUG') == 'True'

from socket import gethostname
ALLOWED_HOSTS = [
    gethostname(), # For internal OpenShift load balancer security purposes.
    os.environ.get('OPENSHIFT_APP_DNS'), # Dynamically map to the OpenShift gear name.
    #'example.com', # First DNS alias (set up in the app)
    #'www.example.com', # Second DNS alias (set up in the app)
]


# Application definition

INSTALLED_APPS = (
    'rest_framework',
    'ciec',
    'C_SADI_CARNOT',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

# GETTING-STARTED: change 'myproject' to your project name:
ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if ON_OPENSHIFT:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.mysql',
            'OPTIONS': {
                'sql_mode': 'traditional',
            },
            'NAME':     os.environ['OPENSHIFT_APP_NAME'],
            'USER':     os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
            'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
            'HOST':     os.environ['OPENSHIFT_MYSQL_DB_HOST'],
            'PORT':     os.environ['OPENSHIFT_MYSQL_DB_PORT'],
        }
    }
else:
   DATABASES = {
    	'default': {
        	'ENGINE': 'django.db.backends.mysql',
        	'NAME': 'admin',
        	'USER': 'root',
        	'PASSWORD': 'valeria1',
        	'HOST': 'localhost',
        	'PORT': '3306'
    	}
    }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (
    '/Library/Python/2.7/site-packages/django/contrib/admin/static/',
)

STATIC_ROOT = '/Users/danielcruzmx/sadicarnot/ultimoSadi/wsgi/static/'

STATIC_URL = '/static/'

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(WSGI_DIR, 'static')
