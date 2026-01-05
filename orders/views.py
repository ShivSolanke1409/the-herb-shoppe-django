from django.shortcuts import redirect, render, get_object_or_404
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

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required
def payment_demo(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == "POST":
        order.status = "Paid"
        order.save()
        return redirect('orders:my_orders')

    return render(request, 'orders/payment_demo.html', {'order': order})