from django.contrib import admin

# Register your models here.
from apps.order.models import Order, Payment

admin.site.register(Order)
admin.site.register(Payment)
