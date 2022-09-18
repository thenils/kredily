from django.db import models

from apps.base.models import BaseModel, BaseOrderModel


class Payment(BaseModel):
    PAYMENT_CHOISES = (
        (1, 'Debit/Credit cards'),
        (2, 'EMI'),
        (3, 'UPI'),
        (4, 'CASH ON DELIVERY')
    )
    success = models.BooleanField(default=True)
    isRefund = models.BooleanField(default=True)
    method = models.IntegerField(choices=PAYMENT_CHOISES, default=4)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)


class Order(BaseOrderModel):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    success = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    payment = models.ForeignKey(Payment, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.product.name}, {self.createdAt}, {self.success}, {self.delivered}'
