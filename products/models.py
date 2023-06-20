from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    title = models.TextField(max_length=400) 
    price = models.IntegerField()
    image = models.FileField(upload_to='products/', null=True, blank=True, verbose_name='Product Image')
    
    def __str__(self):
        return self.name
    
