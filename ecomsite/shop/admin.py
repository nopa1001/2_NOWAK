from django.contrib import admin
from .models import Products, Order, Coupon

# Register your models here.

admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Coupon)