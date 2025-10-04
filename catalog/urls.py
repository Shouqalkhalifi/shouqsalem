from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.product_list, name="product_list"),  # الآن /catalog/ يعمل
    path("products/", views.product_list, name="product_list"),
]
