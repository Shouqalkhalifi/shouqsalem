from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-5uk7#ciq1l78cucq6-8vwm&56%nopo!3uyebg+fa_*l-d&$8bq'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات الخاصة بالمشروع
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
        # مسارات القوالب التي وضعتِها
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# تعريف موديل المستخدم المخصص
AUTH_USER_MODEL = "identity.Account"


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


# اللغة والتوقيت
LANGUAGE_CODE = 'ar'        # تعريب الواجهة
TIME_ZONE = 'Asia/Riyadh'   # توقيت الرياض
USE_I18N = True
USE_TZ = True


# الملفات الثابتة Static
STATIC_URL = '/static/'                         # رابط الوصول للملفات الثابتة
STATICFILES_DIRS = [BASE_DIR / 'static']        # مجلد التطوير (ضع فيه css/js/images)
STATIC_ROOT = BASE_DIR / 'staticfiles'          # مجلد الجمع عند الإنتاج (collectstatic)


# الملفات المرفوعة (وسائط المستخدم Media)
MEDIA_URL = '/media/'                           # الرابط على الويب
MEDIA_ROOT = BASE_DIR / 'media'                 # المجلد المحلي لحفظ الصور/الملفات

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
