from product.models import Category, Brand, Product, ProductImage
from csv import reader
from django.contrib.auth.models import User
import os

# name - Brand - Price - image_url
def run():
    try:
        User.objects.create_superuser(
            username= "Peter",
            password= os.environ.get("password"),
            email= "peter@example.com"
        )
    except:
        x = 1
    ProductImage.objects.all().delete()
    Product.objects.all().delete()
    Category.objects.all().delete()
    Brand.objects.all().delete()
    
    grocery_cat = Category.objects.get_or_create(name = "grocery", slug = "grocery-1", description = "grocery items" )[0]
    upload_carrefour_data(grocery_cat)
    upload_amazon_data(grocery_cat)
    upload_amazon_NonEG()
    
     
def upload_carrefour_data(grocery_cat):
    CSV_DATA_FILES = ['products_beverages-egyptian.csv', 'products_dairy-products.csv',
                      'products_delicatessen-egyptian.csv', 'products_frozen-egyptian.csv',
                      'products_fruits-veg-egyptian.csv', 'products_grocery-egyption.csv']
    for file_name in CSV_DATA_FILES:
        with open(file_name, 'r') as file:
            csvreader = reader(file, delimiter=',')
            next(csvreader)
            
            for row in csvreader:
                product_name, brand_name, price, image_url, country = row[0], row[1], row[2], row[3], row[4]
                price = price[:-4:]
                if price == '':
                    price = '10'
                brand = Brand.objects.get_or_create(name = brand_name, slug = brand_name + "-1", country='EG')

                slug = ''.join(e for e in product_name if (e.isalnum() or e == ' '))
                
                product = Product.objects.get_or_create(name = product_name, 
                slug = slug.replace(' ', '_') + "-1",
                price = float(price), brand = brand[0],
                description = product_name,
                category = grocery_cat
                )
                
                image = ProductImage.objects.get_or_create(image_url=image_url, product = product[0], alt = product_name)

def upload_amazon_data(grocery_cat):
    with open("products.csv", 'r') as file:
        csvreader = reader(file, delimiter=',')
        next(csvreader)
        
        for row in csvreader:
            product_name, brand_name, price, image_url, country = row[0], row[1], row[3], row[4], row[5]
            price = price[4::]
            if price == '':
                price = '10'
            brand = Brand.objects.get_or_create(name = brand_name, slug = brand_name + "-1", country='CN')

            slug = ''.join(e for e in product_name if (e.isalnum() or e == ' '))
            
            product = Product.objects.get_or_create(name = product_name, 
            slug = slug.replace(' ', '_') + "-1",
            price = float(price), brand = brand[0],
            description = product_name,
            category = grocery_cat
            )
            
            image = ProductImage.objects.get_or_create(image_url=image_url, product = product[0], alt = product_name)

def upload_amazon_NonEG():
       with open("amazon_india.csv", 'r') as file:
        csvreader = reader(file, delimiter=',')
        next(csvreader)
        
        for row in csvreader:
            product_name, brand_name, price, image_url, country = row[1], row[1], row[4], row[14], 'IN'
            if(len(product_name) > 250):
                product_name = product_name[:250]
            
            brand_name = brand_name.split(' ')[0]
            if(len(brand_name) > 250):
                brand_name = brand_name[:250]
                
            description = row[8]
            price = price[1::].replace(',','')

            brand = Brand.objects.get_or_create(name = brand_name, slug = brand_name + "-1", country=country)

            slug = ''.join(e for e in product_name if (e.isalnum() or e == ' '))
            category_name  = row[2].split('|')[0]

            if(len(category_name) > 250):
                category_name = category_name[:200]
            
            product = Product.objects.get_or_create(name = product_name[:50], 
            slug = slug.replace(' ', '_') + "-1",
            price = float(price), brand = brand[0],
            description = description[:250:],
            category = Category.objects.get_or_create(name = category_name, slug = category_name + "-1", description = category_name )[0]
            )

            try:
                image = ProductImage.objects.get_or_create(image_url=image_url, product = product[0], alt = product_name)
            except:
                print(product[0])
                continue