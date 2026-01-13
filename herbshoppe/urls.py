from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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

# ✅ FORCE MEDIA SERVING IN PRODUCTION (RENDER FIX)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
