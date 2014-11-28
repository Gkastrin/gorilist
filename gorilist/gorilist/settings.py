"""
Django settings for gorilist project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))


#HEROKUUUU
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#HEROKUUUU

# HEROKUUUUUUUUUUUUUUUU
import dj_database_url
DATABASES = {'default': dj_database_url.config()}
# import django.db.backends.postgresql_psycopg2
#
# DATABASES = {
#     'default' : {
#         'ENGINE':'django.db.backends.postgresql_psycopg2',
#         'NAME':os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO','https')
#HEROKUUUUUUUUUUUUUUUUU




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x^)^0rzbz223!$_5$+%&(^(w+=qcfw^%!-ecb2j$oocwc^x(u5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

#HEROKUUUUUUUUUUUUUUUUU
ALLOWED_HOSTS = ['*']
#HEROKUUUUUUUUUUUUUUU

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gorilist',
    'form_utils',
)

# SESSION_ENGINE = ('django.contrib.sessions.backends.signed_cookies')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gorilist.urls'

WSGI_APPLICATION = 'gorilist.wsgi.application'

# TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
# TEMPLATE_DIRS = [os.path.join("/home/gkas/gorilist/gorilist/templates/gorilist",)]

#HEROKUUUUUU
TEMPLATE_DIRS = [os.path.join("templates/gorilist")]
#HEROKUUUUUU

# https://docs.djangoproject.com/en/dev/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/home/gkas/gorilist/gorilist/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR,"/home/gkas/gorilist/gorilist/static"),)

#HEROKUUUUUUU
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join("static")]
# HEROKUUUUUUU
