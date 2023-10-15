from django.shortcuts import render, redirect

from assetManagement.UserManagement.decorator import manager_user_required
from .models import *
# Create your views here.
from datetime import datetime
from django.contrib import messages #import messages
from django import forms
from django.forms import ModelForm
# create_product 


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

        
        


# class ProductForm(forms.Form):
#     category = ProductCategory.objects.all()
    

#     CHOICES = []
       
#     for single in category:
      
#       CHOICES.append((single.id, single.name))
   
    
#     product_name = forms.CharField(label="Your product name", max_length=100)
#     product_description = forms.CharField(label="Your product name", max_length=100)
#     product_price = forms.CharField(label="Your product name", max_length=100)
#     exp_date = forms.DateField(label="Your product date",)
#     product_category = forms.ChoiceField(label="Your product name", choices=CHOICES)








def create_product_with_form(request):

   form = ProductForm(request.POST or None)
   if request.method == 'POST' and form.is_valid():

      form.save()
      messages.success(request, "Product saved Successfully " )
      return redirect('view_product')
   
   else :
      form  = ProductForm()
      data ={
         
         'form':form
      }
   return render(request, 'create_product_with_form.html', data)
   
   
   
def update_product_with_form(request,id):
   product = Products.objects.get(id = id)
   form = ProductForm(request.POST or None)
   
   
   
   if request.method == 'POST' and form.is_valid():

      form.save()
      messages.success(request, "Product saved Successfully " )
      return redirect('view_product')
   
   else :
      form  = ProductForm(instance=product)
      data ={
         
         'form':form
      }
   return render(request, 'create_product_with_form.html', data)
   
   

   
   
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
      'category':category,
      'form':ProductForm()
      
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