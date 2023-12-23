from django.contrib import admin
from .models import PercentCoupon, VoucherCoupon

# Register your models here.
admin.site.register(PercentCoupon)
admin.site.register(VoucherCoupon)