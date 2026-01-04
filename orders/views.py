from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from cart.views import get_cart_items   # we’ll define this helper
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart_items, total = get_cart_items(request)

    if not cart_items:
        return redirect('/')

    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item['product'],
            quantity=item['quantity'],
            price=item['product'].price
        )

    request.session['cart'] = {}
    return redirect('/')
