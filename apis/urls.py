from django.urls import path, include

urlpatterns = [
    path('auth/', include('apis.auth.urls')),
    path('product/', include('apis.product.urls')),
    path('order/', include('apis.order.urls'))

]