from django.urls import path, include

urlpatterns = [
    path('v1/', include('apis.product.v1.urls'))
]