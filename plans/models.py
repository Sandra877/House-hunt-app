from django.db import models

# Create your models here.
class plansmodel(models.Model):
    duration = models.TextField()
    price = models.FloatField()
    promotions = models.CharField(max_length = 150)
    
    