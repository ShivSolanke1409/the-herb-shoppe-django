from django.urls import path
from .views import checkout, my_orders, payment_demo
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('my-orders/', my_orders, name='my_orders'),
    path('pay/<int:order_id>/', payment_demo, name='payment_demo'),
    path('cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
]
