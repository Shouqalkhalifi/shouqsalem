from pathlib import Path
import cloudinary
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# مفاتيح Django
# ========================
SECRET_KEY = config("DJANGO_SECRET_KEY", default="unsafe-secret-key")

DEBUG = config("DJANGO_DEBUG", default=False, cast=bool)

# السماح بالاتصال
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="127.0.0.1,localhost,0.0.0.0",
    cast=Csv()
)

# ========================
# تعريف الموديل المخصص للمستخدم
# ========================
AUTH_USER_MODEL = "identity.Account"

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

    # allauth dependencies
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

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

    # WhiteNoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # لازم هذا لـ allauth
    'allauth.account.middleware.AccountMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========================
# القوالب
# ========================
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
ROOT_URLCONF = 'shouqsalem.urls'

# ========================
# قاعدة البيانات
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# ========================
# static & whitenoise
# ========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ========================
# التخزين عبر Cloudinary
# ========================
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

cloudinary.config(
    cloud_name=config("CLOUDINARY_NAME", default=""),
    api_key=config("CLOUDINARY_KEY", default=""),
    api_secret=config("CLOUDINARY_SECRET", default="")
)

# ========================
# الإعدادات العامة
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ============ django-allauth settings ============
SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_LOGIN_METHODS = {"username", "email"}   # تسجيل الدخول باليوزر أو الإيميل
ACCOUNT_SIGNUP_FIELDS = ["username*", "email", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "none"

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# ========================
# إعدادات البريد
# ========================
if DEBUG:
    # وقت التطوير → الإيميلات تظهر في الـ Terminal
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    # وقت الإنتاج → عبر Gmail SMTP
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="s19413348@gmail.com")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="kyzg qaog wmpa ygun")
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
