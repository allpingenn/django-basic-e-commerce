from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    title = models.TextField(max_length=400) 
    price = models.IntegerField()
    image = models.FileField(upload_to='products/', null=True, blank=True, verbose_name='Product Image')
    
    def __str__(self):
        return self.name