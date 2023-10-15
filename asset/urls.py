
from django.urls import path, include
from .views import create_product,view_product,update_product,delete_product,create_product_with_form,update_product_with_form


urlpatterns = [
    
    path('create_product_with_form/',create_product_with_form,name='create_product_with_form'),
    path('update_product_with_form/<int:id>/',update_product_with_form,name='update_product_with_form'),
    
    path('create_product/',create_product,name='create_product'),
    

    path('view_product/',view_product,name='view_product'),
    path('update_product/<int:id>/',update_product,name='update_product'),
    path('delete_product/<int:id>/',delete_product,name='delete_product'),
]

