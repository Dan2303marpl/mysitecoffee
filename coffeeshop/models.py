
from django.db import models

class Coffe_sort(models.Model):
    sort = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    count = models.IntegerField(blank = True)
    cost = models.FloatField(blank = True)

class ap_equip(models.Model):
    equipment = models.CharField(max_length=100)
    count = models.IntegerField(blank = True)
    cost = models.FloatField(blank = True)

class dop_ap(models.Model):
    sirop = models.CharField(max_length=100)
    cost = models.FloatField(blank = True)
    count = models.IntegerField(blank = True)





   



    
# Create your models here.
