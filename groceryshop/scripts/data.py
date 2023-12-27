from product.models import Category, Brand, Product, ProductImage
from csv import reader


# name - Brand - Price - image_url
def run():
    Category.objects.all().delete()
    Brand.objects.all().delete()
    Product.objects.all().delete()
    
    ProductImage.objects.all().delete()
    grocery_cat = Category.objects.get_or_create(name = "grocery", slug = "grocery-1", description = "grocery items" )[0]
    upload_carrefour_data(grocery_cat)
    upload_amazon_data(grocery_cat)
    
    
     
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
    