from django.db import models
from services.models import Service
# Create your models here.

class Product(models.Model):
    class Choice(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    identity = models.IntegerField(choices=Choice.choices,default=Choice.one)
    name = models.CharField(max_length=120, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    desc1 = models.CharField(max_length=500, blank=True, null=True)
    desc2 = models.CharField(max_length=500, blank=True, null=True)
    desc3 = models.CharField(max_length=500, blank=True, null=True)
    desc4 = models.CharField(max_length=500, blank=True, null=True)
    thumb = models.ImageField(upload_to='product/images/', blank=True, null=True)
    

    def __str__(self):
        return self.name


class Product_detail(models.Model):
    class Choice(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    identity = models.IntegerField(choices=Choice.choices,default=Choice.one)
    name = models.CharField(max_length=120, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    desc1 = models.CharField(max_length=500, blank=True, null=True)
    desc2 = models.CharField(max_length=500, blank=True, null=True)
    desc3 = models.CharField(max_length=500, blank=True, null=True)
    desc4 = models.CharField(max_length=500, blank=True, null=True)
    desc5 = models.CharField(max_length=500, blank=True, null=True)
    thumb = models.ImageField(upload_to='product/images/',blank=True, null=True)
    mob_thumb =  models.ImageField(upload_to='product/images/',blank=True, null=True)
    

    def __str__(self):
        return self.name