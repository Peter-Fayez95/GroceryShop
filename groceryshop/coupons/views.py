from django.shortcuts import render
from .models import PercentCoupon, VoucherCoupon

# Create your views here.
def coupons_list(request):
    user = request.user
    return render(request, "coupons/list.html", {
        'percent_coupons': PercentCoupon.objects.filter(user=user).all(),
        'voucher_coupons': VoucherCoupon.objects.filter(user=user).all(),
    })