from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.category_products, name='category_filter'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
