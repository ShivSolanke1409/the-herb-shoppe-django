from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product_id = str(product_id)
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {'quantity': 1}

    request.session['cart'] = cart
    return redirect('cart:cart_detail')



def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for product_id, item in cart.items():
        product = get_object_or_404(Product, id=product_id)
        product.quantity = item['quantity']
        product.subtotal = product.price * product.quantity
        total += product.subtotal
        products.append(product)

    return render(request, 'cart/cart_detail.html', {
        'products': products,
        'total': total
    })

def get_cart_items(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for product_id, item in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * item['quantity']
        total += subtotal
        items.append({
            'product': product,
            'quantity': item['quantity'],
            'subtotal': subtotal
        })

    return items, total
