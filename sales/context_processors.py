from typing import Dict, Any
from django.http import HttpRequest


def cart_context(request: HttpRequest) -> Dict[str, Any]:
    """Provide cart_count to all templates based on session cart structure.

    Expected session structure:
    request.session['cart'] = {
        str(product_id): { 'qty': int, ... }  OR  str(product_id): int
    }
    We safely sum integers or nested dict['qty'] values.
    """
    cart = request.session.get('cart') or {}
    count = 0
    try:
        if isinstance(cart, dict):
            for _, v in cart.items():
                if isinstance(v, dict):
                    qty = v.get('qty', 0)
                    if isinstance(qty, int):
                        count += qty
                elif isinstance(v, int):
                    count += v
    except Exception:
        # Be robust in case of unexpected session content
        count = 0
    return {"cart_count": count}
