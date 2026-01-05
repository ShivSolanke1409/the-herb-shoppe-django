from django.urls import path
from .views import checkout, my_orders, payment_demo

app_name = 'orders'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('my-orders/', my_orders, name='my_orders'),
    path('pay/<int:order_id>/', payment_demo, name='payment_demo'),
]
