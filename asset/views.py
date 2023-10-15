from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from datetime import datetime
from django.contrib import messages #import messages
# create_product 

def create_product(request):
   category = ProductCategory.objects.all()
   
   
   if request.method == "POST":
      product_name = request.POST.get('product_name')
      product_description = request.POST.get('product_description')
      product_price = request.POST.get('product_price')
      exp_date = request.POST.get('exp_date')
      product_category = request.POST.get('product_category')
      
      
      obj = Products()
      
      obj.product_name = product_name
      obj.product_description = product_description
      obj.product_price = product_price
      obj.exp_date = exp_date
      obj.product_category = ProductCategory.objects.get(id =product_category )
      
      obj.save()
      messages.success(request, "Product saved Successfully " )
      return redirect('view_product')
   data = {
      'category':category
      
   }
   return render(request,'create_product.html', data)
   
   
   
def view_product(request):

   products = Products.objects.all()
   
   return render(request,'view_product.html',{'products':products,})



def update_product(request, id):
   
   
   category = ProductCategory.objects.all()
   
   product = Products.objects.get(id = id)
   
   if request.method == "POST":
      product_name = request.POST.get('product_name')
      product_description = request.POST.get('product_description')
      product_price = request.POST.get('product_price')
      exp_date = request.POST.get('exp_date')
      product_category = request.POST.get('product_category')

      obj = product
      
      obj.product_name = product_name
      obj.product_description = product_description
      obj.product_price = product_price
      obj.exp_date = exp_date

 
      obj.product_category = ProductCategory.objects.get(id =product_category )
      
      obj.save()
      messages.success(request, "Product updated Successfully " )
      return redirect('view_product')
      

   
   
   return render(request,'update_product.html',{'product':product,'category':category})



def delete_product(request, id):
   product = Products.objects.get(id = id)
   product.delete()
   messages.success(request, "Product deleted Successfully " )
   return redirect('view_product')