from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views   # استدعاء view الرئيسي

urlpatterns = [
    # الرئيسية
    path('', views.home_view, name='home'),

    # لوحة التحكم
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('identity/', include('identity.urls')),
    path('catalog/', include('catalog.urls')),
    path('sales/', include('sales.urls')),
]

# إضافة روابط static و media في بيئة التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
