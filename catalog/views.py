from django.shortcuts import render
from .models import Product


def product_list(request):
    """عرض جميع المنتجات وتمريرها إلى القالب"""
    products = Product.objects.all()
    return render(request, "catalogt/product_list.html", {"products": products})
