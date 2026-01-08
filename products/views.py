from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

def product_list(request, category_slug=None):
    query = request.GET.get('q')
    categories = Category.objects.all()
    products = Product.objects.all()

    # Category filter
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        products = products.filter(category=category)
    else:
        category = None

    # Search filter
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        'products': products,
        'categories': categories,
        'category': category,
        'query': query,
    }

    return render(request, 'products/product_list.html', context)



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'products/product_detail.html', {'product': product})
