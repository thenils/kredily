from django.urls import path, include

urlpatterns = [
    path('v1/', include('apis.order.v1.urls'))
]