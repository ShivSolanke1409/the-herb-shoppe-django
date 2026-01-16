from django.contrib import admin
from django.urls import path, include
from pages.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # CORE PAGES
    path('', home, name='home'),

    # APP ROUTES
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
]
