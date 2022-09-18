from rest_framework import generics
from rest_framework.permissions import AllowAny

from apis.auth.v1.serializer import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["request"] = self.request
        return context