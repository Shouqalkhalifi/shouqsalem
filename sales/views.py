from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Favorite, Order
from catalog.models import Product
from django.contrib import messages

def cart_view(request):
    # إضافة إلى السلة عبر بارامتر ?add=<product_id>
    add_id = request.GET.get("add")
    if add_id:
        product = get_object_or_404(Product, id=add_id)
        cart = request.session.get("cart", {})
        cart[str(product.id)] = cart.get(str(product.id), 0) + 1
        request.session["cart"] = cart
        messages.success(request, f"تمت إضافة ‘{product.name}’ إلى السلة بنجاح")
        return redirect("sales:cart")

    # تجهيز بيانات السلة للعرض
    cart = request.session.get("cart", {})
    ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(id__in=ids)
    items = []
    total = 0
    for p in products:
        qty = cart.get(str(p.id), 0)
        line_total = float(p.price) * qty
        total += line_total
        items.append({"product": p, "qty": qty, "line_total": line_total})

    context = {"items": items, "total": total}
    return render(request, "sales/cart.html", context)


@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(account=request.user).select_related("product")
    context = {"favorites": favorites}
    return render(request, "sales/favorites.html", context)


@login_required
def toggle_favorite(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    fav, created = Favorite.objects.get_or_create(account=request.user, product=product)
    if not created:
        fav.delete()
    # رجوع إلى الصفحة السابقة إن وُجدت
    next_url = request.GET.get("next") or request.META.get("HTTP_REFERER") or "/"
    return redirect(next_url)


@login_required
def orders_list(request):
    orders = (
        Order.objects.filter(account=request.user)
        .prefetch_related("items__product")
        .order_by("-created_at")
    )
    return render(request, "sales/orders.html", {"orders": orders})
