import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'mcvc1cs@fhf3shj&$1sp=l=nj^t2r1=1%55pe9x0eghfukm!9m'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'blog',
    'mptt',
    'tinymce',
    'ckeditor',
# Django sites framework is required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
]

SOCIALACCOUNT_PROVIDERS = {'facebook': {}, 'google':{}, 'twitter':{}}

# Ensure SITE_ID is set sites app 
SITE_ID = 1

# Add the 'allauth' backend to AUTHENTICATION_BACKEND and keep default ModelBackend
AUTHENTICATION_BACKENDS = [ 'django.contrib.auth.backends.ModelBackend',
                           'allauth.account.auth_backends.AuthenticationBackend'] 
# EMAIL_BACKEND so allauth can proceed to send confirmation emails
# ONLY for development/testing use console 
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

# Custom allauth settings
# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'email' 
ACCOUNT_EMAIL_REQUIRED = True

# Make email verification mandatory to avoid junk email accounts
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' 

# Eliminate need to provide username, as it's a very old practice
ACCOUNT_USERNAME_REQUIRED = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'core.urls'
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
                'blog.views.category_list',
                'accounts.views.avatar'
            ],
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }

}
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
LOGIN_REDIRECT_URL = 'accounts:profile'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



