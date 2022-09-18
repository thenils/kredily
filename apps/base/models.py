from django.contrib.auth.models import User
from django.db import models

from apps.product.models import Product


class BaseModel(models.Model):
    createdAt = models.DateTimeField(auto_now=True, editable=False)
    updateAt = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class BaseOrderModel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, editable=False)
    createdAt = models.DateTimeField(auto_now=True, editable=False)
    updateAt = models.DateTimeField(auto_now_add=True)
    isDeleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


def get_address_json():
    return {}
