from django.shortcuts import render
from products.models import Product, Category

def home(request):
    trending = Product.objects.filter(is_trending=True, is_available=True)[:8]
    featured = Product.objects.filter(is_featured=True, is_available=True)[:8]
    categories = Category.objects.filter(is_active=True)

    return render(request, 'pages/home.html', {
        'trending': trending,
        'featured': featured,
        'categories': categories,
    })
