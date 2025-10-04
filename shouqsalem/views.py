from django.shortcuts import render
from catalog.models import Product

def home_view(request):
    """
    الصفحة الرئيسية للمتجر:
    - تعرض المنتجات الرقمية
    - تعرض المنتجات الملموسة
    """
    digital_products = Product.objects.filter(category__name__icontains="منتجات رقمي")
    physical_products = Product.objects.filter(category__name__icontains="ملموسة")

    context = {
        "digital_products": digital_products,
        "physical_products": physical_products,
    }
    return render(request, "home.html", context)
