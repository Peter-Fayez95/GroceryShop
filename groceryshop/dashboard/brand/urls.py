from django.urls import path
from . import views

from dashboard.decorators import user_dashboard_permission 

app_name = 'brand_dashboard'

urlpatterns = [
    path('create/', user_dashboard_permission(views.CreateBrand.as_view()), name = 'create_brand'),
    
]
