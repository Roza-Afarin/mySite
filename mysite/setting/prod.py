from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1m^8w+7cur)i3&)5wg5(&e&=7p+9+w*19%jm%c(qysl)l9l8m_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


#sitemap
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_ROOT = BASE_DIR / 'media/'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

SESSION_COOKIE_SECURE=True