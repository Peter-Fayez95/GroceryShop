from django.urls import path
from .views import coupons_list

app_name = "coupons"

urlpatterns = [
    path('', coupons_list, name="coupons_list"),
]
