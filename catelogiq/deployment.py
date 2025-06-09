import os
from .settings import *
from .settings import BASE_DIR

SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

# Azure and Databricks credentials
AZURE_ACCOUNT_NAME = os.environ['AZURE_ACCOUNT_NAME'] #config('AZURE_ACCOUNT_NAME')
AZURE_ACCOUNT_KEY = os.environ['AZURE_ACCOUNT_KEY'] #config('AZURE_ACCOUNT_KEY')
AZURE_FILE_SYSTEM = os.environ['AZURE_FILE_SYSTEM'] #config('AZURE_FILE_SYSTEM')
#DATABRICKS_HOST = os.environ['DATABRICKS_HOST'] #config('DATABRICKS_HOST')
#DATABRICKS_TOKEN = os.environ['DATABRICKS_TOKEN'] #config('DATABRICKS_TOKEN')


# Databricks settings
DATABRICKS_HOST = os.environ['DATABRICKS_HOST'] #'https://adb-3623933893880845.5.azuredatabricks.net'
DATABRICKS_TOKEN = os.environ['DATABRICKS_TOKEN'] #'dapi44c5e998d105e25008af210c77e37f3a-3'
DATABRICKS_HTTP_PATH = os.environ['DATABRICKS_HTTP_PATH'] #'/sql/1.0/warehouses/50e55df2f9229a9e'
DATABRICKS_DASHBOARD_ID = os.environ['DATABRICKS_DASHBOARD_ID'] #'01f031711a751af7876b9008149aa390'  # your dashboard id
DATABRICKS_WORKSPACE_URL = os.environ['DATABRICKS_WORKSPACE_URL'] #'https://adb-3623933893880845.5.azuredatabricks.net'  # your workspace URL
DATABRICKS_CLUSTER_ID = os.environ['DATABRICKS_CLUSTER_ID'] #config('DATABRICKS_CLUSTER_ID')


# Temporary file storage
TEMP_DIR = BASE_DIR / 'temp'
SECRET_KEY = 'mhot9pl*(mz1pc$@xve9qn%v2ogy6cj%-$5wrha0#(4#rlu_6v'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

WSGI_APPLICATION = 'catelogiq.wsgi.application'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (str(BASE_DIR.joinpath('staticfiles')),)
STATIC_URL = '/staticfiles/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
