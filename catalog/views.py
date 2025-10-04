from django.shortcuts import render
from django.db.models import Q
from .models import Product
from django.shortcuts import get_object_or_404

def product_list(request):
    products = Product.objects.all()

    p_type = request.GET.get("type")
    q = request.GET.get("q")
    cat = request.GET.get("category")

    # هنا نخليها نفس منطق الهوم: التصفية بالاسم
    if p_type == "digital":
        products = products.filter(category__name__icontains="digital")
    elif p_type == "physical":
        products = products.filter(category__name__icontains= "physical")

    if q:
        products = products.filter(Q(name__icontains=q) | Q(description__icontains=q))

    if cat:
        products = products.filter(category__slug=cat)

    context = {
        "products": products,
        "selected_type": p_type,
        "query": q or "",
        "selected_category": cat or "",
        "count": products.count(),
    }

    return render(request, "catalogt/product_list.html", context)


def product_detail(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalogt/product_detail.html", {"product": product})
