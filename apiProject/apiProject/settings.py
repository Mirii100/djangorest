
import dj_database_url
from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
#'django-insecure-izr5i)9jnnqksgr14fumsml$4v#9=+p6onq1(remykt62pe38+'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG','False').lower()=='true'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS','').split()


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basic',
    'rest_framework',
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

ROOT_URLCONF = 'apiProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'apiProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'demoApi',
#         'USER': 'postgres',
#         'PASSWORD': 'alex',
#         'HOST': 'localhost',  # Or your DB server
#         'PORT': '5432',       # Default PostgreSQL port
#     }
# }
DATABASE_URL=os.environ.get('DATABASE_URL')
DATABASES['default']=dj_database_url.parse(DATABASE_URL)
#postgresql://djangoapi_bpk7_user:5piru4uVRdXLKg9CYwCrp6lWEaAgq27l@dpg-cvhro30gph6c73cf05ng-a.oregon-postgres.render.com/djangoapi_bpk7
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoapi_bpk7',  # Database name
        'USER': 'djangoapi_bpk7_user',  # Username
        'PASSWORD': '5piru4uVRdXLKg9CYwCrp6lWEaAgq27l',  # Password
        'HOST': 'dpg-cvhro30gph6c73cf05ng-a.oregon-postgres.render.com',  # Host
        'PORT': '5432',  # Default PostgreSQL port
    }
}


if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'djangoapi_bpk7',
            'USER': 'djangoapi_bpk7_user',
            'PASSWORD': '5piru4uVRdXLKg9CYwCrp6lWEaAgq27l',
            'HOST': 'dpg-cvhro30gph6c73cf05ng-a.oregon-postgres.render.com',
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
