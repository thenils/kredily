from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apis.order.v1.serializer import OrderWOSerializer, OrderROSerializer
from apps.order.service import OrderService
from apps.product.models import Product
from utils.pagination import get_paginated_response, LimitOffsetPagination


class OrderView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializers = {
        'WOSerializer': OrderWOSerializer,
        'ROSerializer': OrderROSerializer
    }
    orderService = OrderService()

    def post(self, request):
        serializer = OrderWOSerializer(data=request.POST)
        if serializer.is_valid():
            data = serializer.data
            product = Product.objects.get(id=data['product'])
            _, message = self.orderService.create(request.user, product, data['quantity'])
            if _:
                return Response({'status': True, 'message': message}, status=status.HTTP_201_CREATED)
            return Response({'status': False, 'message': message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors)

    def get(self, request):

        return get_paginated_response(
            pagination_class=LimitOffsetPagination,
            serializer_class=OrderROSerializer,
            queryset=self.orderService.retrive(user=request.user),
            request=request,
            view=self)

