from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default='SOME STRING')
    price = models.IntegerField()
    amount = models.PositiveIntegerField(default=0)
    category = models.TextField()
    description = models.TextField()
    date_added = models.DateField(auto_now_add=True)