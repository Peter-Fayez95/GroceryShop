from django.db import models
from userprofile.models import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class PercentCoupon(models.Model):
    percent = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user = models.ForeignKey(get_user_model(), 
                             on_delete=models.CASCADE,
                             related_name="percent_coupons")
    
    def __str__(self):
        return f"{self.percent}% Discount"
    
    
class VoucherCoupon(models.Model):
    amount = models.IntegerField()
    user = models.ForeignKey(get_user_model(), 
                             on_delete=models.CASCADE,
                             related_name="voucher_coupons")
    
    def __str__(self):
        return f"EGP {self.amount} Discount"