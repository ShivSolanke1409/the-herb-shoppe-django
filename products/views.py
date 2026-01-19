from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category


def product_list(request, category_slug=None):
    query = request.GET.get('q', '').strip()
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        category = None

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'category': category,
        'query': query,
    })


def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug, is_active=True)
    categories = Category.objects.filter(is_active=True)
    products = Product.objects.filter(category=category, is_available=True)

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'category': category,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'products/product_detail.html', {'product': product})
