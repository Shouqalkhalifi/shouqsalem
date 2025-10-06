from pathlib import Path
import cloudinary
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# مفاتيح Django
# ========================
SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = config("DJANGO_DEBUG", default="False").lower() == "true"
ALLOWED_HOSTS = ["*"]

# ========================
# التطبيقات المثبتة
# ========================
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

# ========================
# الوسطاء
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise Middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',

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

# ========================
# قاعدة البيانات
# ========================
if DEBUG:
    # التطوير: SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # الإنتاج: PostgreSQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': config("DB_HOST"),
            'PORT': config("DB_PORT", default=5432, cast=int),
            'NAME': config("DB_NAME"),
            'USER': config("DB_USER"),
            'PASSWORD': config("DB_PASSWORD"),
        }
    }

# ========================
# موديل المستخدم
# ========================
AUTH_USER_MODEL = "identity.Account"

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================
# اللغة والتوقيت
# ========================
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True

# ========================
# الملفات الثابتة
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise لتقديم الملفات الثابتة في الإنتاج
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ========================
# التخزين عبر Cloudinary
# ========================
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media/'

# إعداد مفاتيح Cloudinary من env
cloudinary.config(
    cloud_name=config("CLOUDINARY_NAME"),
    api_key=config("CLOUDINARY_KEY"),
    api_secret=config("CLOUDINARY_SECRET")
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
