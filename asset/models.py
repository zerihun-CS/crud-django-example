from django.db import models

# Create your models here.

class ProductCategory(models.Model):
   name  = models.CharField(max_length=50)
   
   def __str__(self):
      return self.name

class Products( models.Model):
   product_name = models.CharField( max_length=150)
   product_description = models.CharField( max_length=650)
   product_price = models.FloatField()
   exp_date  = models.DateField(null=True)
   product_category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE)
   def __str__(self):
      return self.product_name
