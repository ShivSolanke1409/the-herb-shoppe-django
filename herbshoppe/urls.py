from django.contrib import admin
from django.urls import path, include
from pages.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    path('', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
]
