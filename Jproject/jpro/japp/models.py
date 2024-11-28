from django.db import models
 
# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
 
    def __str__(self) -> str:
        return self.username
 
class Pro(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
 
    def __str__(self) -> str:
        return self.name