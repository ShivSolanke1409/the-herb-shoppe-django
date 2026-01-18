from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.views import get_cart_items   # we’ll define this helper
from .models import Order, OrderItem
from django.db.models import Q



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
    return render(request, 'orders/payment_demo.html', {'order': order})


@login_required
def my_orders(request):
    query = request.GET.get('q')

    orders = Order.objects.filter(user=request.user)

    if query:
        orders = orders.filter(
            Q(id__icontains=query) |
            Q(items__product__name__icontains=query)
        ).distinct()

    return render(request, 'orders/my_orders.html', {
        'orders': orders,
        'search_context': 'orders',   # ✅
    })




@login_required
def payment_demo(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == "POST":
        order.status = "Paid"
        order.save()
        return redirect('orders:my_orders')

    return render(request, 'orders/payment_demo.html', {'order': order})

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status == "Pending":
        order.status = "Cancelled"
        order.save()

    return redirect('orders:my_orders')