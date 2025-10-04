from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path("cart/", views.cart_view, name="cart"),
    path("favorites/", views.favorites_list, name="favorites"),
    path("favorites/toggle/<int:product_id>/", views.toggle_favorite, name="toggle_favorite"),
    path("orders/", views.orders_list, name="orders"),
]
