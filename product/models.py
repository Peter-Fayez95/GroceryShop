from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.text import slugify
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from django_countries.fields import CountryField
from datetime import date, timedelta
import uuid

fields = ["name", "description", "background_image"]

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to = 'category_background', 
                                         blank = True, null = True
    )
    parent = models.ForeignKey(
        'self', 
        blank = True,
        null = True, 
        on_delete = models.CASCADE
    )
    
    tree = TreeManager()
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse_lazy("dashboard:category_dashboard:category_list") 
    
# First
class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(blank = True)
    country = CountryField(blank = True)
    
    def get_absolute_url(self):
        return reverse_lazy("dashboard:brand_dashboard:create_brand")
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(default = '')
    price = models.FloatField(default=0)
    weight = models.FloatField(default = 1)
    # sku needs more work
    sku = models.UUIDField(default = uuid.uuid4, unique = True, editable = True)
    stock = models.PositiveIntegerField(default = 5)
    brand = models.ForeignKey('Brand',on_delete= models.CASCADE, null = True)
    category = models.ForeignKey('Category',on_delete= models.CASCADE, null = True)
    exp_date = models.DateField('exp_date', default = date.today() + timedelta(days = 25))
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("dashboard:product_dashboard:product_list")
    
    def get_thumbnail(self):
        return self.productimage_set.first() 

    @property
    def expired(self):
        '''
        return 
        0: already expired
        1: about to expire
        2: more than 30 days before expiratin        
        '''
        # return 1
        if self.exp_date  <= date.today():
            return 0
        elif self.exp_date > timedelta(30) + date.today():
            return 2
        else:
            return 1
    
    @property
    def discounted_price(self):
        return    round(0.95 * self.price, 2)
    
# name - image url - price - brand
    
class ProductImage(models.Model):
    # image = models.ImageField(blank = True, null = True)
    image_url = models.URLField(blank = True)
    product = models.ForeignKey('Product', on_delete = models.CASCADE)
    alt = models.CharField(max_length = 225)
    
