from django.urls import path

from .views import detail_product, add_product_to_checkout, ListProduct

app_name = "products"

urlpatterns = [
    path('<str:slug>/', detail_product,name="detail_product"),
    path('category/<str:slug>/', ListProduct.as_view(),name="list_product"),
    path('add/<int:pk>/', add_product_to_checkout, name="add_product_to_checkout"),
    
]