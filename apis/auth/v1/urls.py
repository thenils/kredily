from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from apis.auth.v1.serializer import CustomJWTSerializer
from apis.auth.v1.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register-user'),
    path('token/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]