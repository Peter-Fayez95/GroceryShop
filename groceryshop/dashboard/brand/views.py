from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, ListView
from product.models import Brand
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

class CreateBrand(CreateView):
    model = Brand
    template_name = "dashboard/brand/create.html"
    fields = ["name", 'image']
    
    def form_valid(self, form):
        instance = form.save()
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        
        return super(CreateBrand, self).form_valid(form)
    

class UpdateBrand(UpdateView):
    model = Brand
    template_name = "dashboard/brand/create.html"
    fields = ["name", 'image']
    
    def form_valid(self, form):
        instance = form.instance
        instance.slug = slugify(instance.name) + "-" + str(instance.id)
        instance.save()
        
        return super(UpdateBrand, self).form_valid(form)
    
class ListBrand(ListView):
    model = Brand
    template_name = "dashboard/brand/list.html"
    

def delete_brand(request,pk):
    brand = get_object_or_404(Brand,pk=pk) 
    if brand:
        brand.delete()
        return JsonResponse({'message' : 'the brand has been deleted successfully'},status=200)
    
    return JsonResponse({'message':'this brand instance does not exist'}, status=400)