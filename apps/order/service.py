from django.contrib.auth.models import User

from apps.order.models import Order
from apps.product.models import Product


class OrderService:
    model = Order

    def retrive(self, user: User):
        qs = self.model.objects.filter(user=user).order_by('-createdAt')
        return qs

    def create(self, user: User, product: Product, q: int):
        if product.quantity < q:
            return False, 'Product is Available'
        self.model.objects.create(user=user, product=product, quantity=q, success=True, delivered=True,
                                  amount=product.price * q)
        product.quantity = product.quantity - q
        product.save()
        return True, 'order created successfully'
