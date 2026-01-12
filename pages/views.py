from django.shortcuts import render
from products.models import Product, Category

def home(request):
    trending_products = Product.objects.filter(is_trending=True, is_available=True)[:8]
    featured_products = Product.objects.filter(is_featured=True, is_available=True)[:8]
    categories = Category.objects.filter(is_active=True)

    return render(request, 'pages/home.html', {
        'trending_products': trending_products,
        'featured_products': featured_products,
        'categories': categories,
    })
