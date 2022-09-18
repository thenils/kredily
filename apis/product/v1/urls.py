from django.urls import path

from apis.product.v1.views import ProductView

urlpatterns = [
    path('', ProductView.as_view(), name='retrieve-product')
]
