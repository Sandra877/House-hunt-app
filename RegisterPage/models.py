from django.db import models

# Create your models here.
class register_model(models.Model):
    name = models.CharField(max_length = 2000)
    email = models.EmailField()
    password = models.CharField(max_length = 50)
    
    