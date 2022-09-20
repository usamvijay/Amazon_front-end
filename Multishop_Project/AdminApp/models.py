from django.db import models

# Create your models here.

class Catagories(models.Model):
    Category        =   models.TextField(max_length=50)
    Category_image  =   models.ImageField(upload_to = 'media/categories/')
    createdAt       =   models.DateTimeField(auto_now_add=True)



class Products(models.Model):
    cat_id           =  models.ForeignKey(Catagories, on_delete=models.CASCADE, default=1)
    item_image       =  models.ImageField(upload_to = 'media/products/')
    item_name        =  models.CharField(max_length=60)
    Descount_price   =  models.ImageField(max_length=60)
    Original_price   =  models.IntegerField()
    Qty              =  models.CharField(max_length=60)
    Discription      =  models.CharField(max_length=600)
    createdAt        =  models.DateTimeField(auto_now_add=True)