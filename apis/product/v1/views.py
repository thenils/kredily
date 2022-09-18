from django.core.exceptions import FieldError
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apis.product.v1.serializer import ProductReadOnlySerializer
from apps.product.models import Product
from utils.pagination import get_paginated_response, LimitOffsetPagination


class ProductView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductReadOnlySerializer

    def get(self, request, *args, **kwargs):
        order_by = request.GET.get('sort_field', 'id')
        order_reverse = '-' if request.GET.get('sort_asc', None) == 'true' else ''
        order = f'{order_reverse}{order_by}'
        try:
            queryset = Product.objects.all().order_by(order)
        except FieldError as e:
            return Response({'success': False, 'message': e.args}, status=status.HTTP_400_BAD_REQUEST)

        return get_paginated_response(
            pagination_class=LimitOffsetPagination,
            serializer_class=self.serializer_class,
            queryset=queryset,
            request=request,
            view=self
        )
