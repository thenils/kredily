from rest_framework import serializers

from apps.order.models import Order
from apps.product.models import Product


class OrderWOSerializer(serializers.Serializer):
    product = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True)

    class Meta:
        fields = ['product', 'quantity']

    def validate(self, attrs):
        try:
            product = Product.objects.get(id=attrs['product'])
        except Exception as e:
            raise serializers.ValidationError({'product': ['Product not found!']})
        if product and product.quantity >= attrs['quantity']:
            return attrs
        raise serializers.ValidationError({'quantity': ['order quantity is higher']})


class OrderROSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
