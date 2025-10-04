from django.shortcuts import render
from catalog.models import Product
from django.db.models import Q

def home_view(request):
    all_products = Product.objects.all()
    # التصفية بالاسم (دعم العربية والإنجليزية)
    digital_products = Product.objects.filter(
        Q(category__name__icontains="digital") | Q(category__name__icontains="رقمي")
    )
    physical_products = Product.objects.filter(
        Q(category__name__icontains="physical") | Q(category__name__icontains="ملموس")
    )

    context = {
        "all_products": all_products,
        "digital_products": digital_products,
        "physical_products": physical_products,
    }
    return render(request, "home.html", context)
