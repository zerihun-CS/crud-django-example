
from django.urls import path, include
from .views import create_product,view_product,update_product,delete_product


urlpatterns = [
    
    path('create_product/',create_product,name='create_product'),
    path('view_product/',view_product,name='view_product'),
    path('update_product/<int:id>/',update_product,name='update_product'),
    path('delete_product/<int:id>/',delete_product,name='delete_product'),
]

