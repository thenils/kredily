from django.urls import path

from apis.order.v1.views import OrderView

urlpatterns = [
    path('', OrderView.as_view(), name='order-actions'),
]