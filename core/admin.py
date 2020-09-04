from django.contrib import admin
from . import models

#Registe Models
admin.site.register(models.Item)
admin.site.register(models.OrderItem)
admin.site.register(models.Order)
admin.site.register(models.Coupon)