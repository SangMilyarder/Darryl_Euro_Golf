from django.db import models
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default='SOME STRING')
    price = models.IntegerField()
    amount = models.IntegerField()
    category = models.TextField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)