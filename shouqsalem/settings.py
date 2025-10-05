from pathlib import Path
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح Django
SECRET_KEY = 'django-insecure-5uk7#ciq1l78cucq6-8vwm&56%nopo!3uyebg+fa_*l-d&$8bq'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # مكتبات خارجية
    'cloudinary',
    'cloudinary_storage',

    # تطبيقات المشروع
    'identity',
    'catalog',
    'sales',
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

ROOT_URLCONF = 'shouqsalem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'templates' / 'identityt',
            BASE_DIR / 'templates' / 'catalogt',
            BASE_DIR / 'templates' / 'sales',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sales.context_processors.cart_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'shouqsalem.wsgi.application'


# قاعدة البيانات SQLite (ممكن تبدلها لاحقاً)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# موديل المستخدم
AUTH_USER_MODEL = "identity.Account"

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# التخزين عبر Cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

MEDIA_URL = '/media/'

# إعداد مفاتيح Cloudinary
cloudinary.config(
    cloud_name="daaxif6wc",
    api_key="286238597463312",
    api_secret="kONm5K0vSN8rVDnHI_XTQ1es0gA"
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
