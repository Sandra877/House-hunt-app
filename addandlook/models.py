from django.db import models

# Create your models here.
class House(models.Model):
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
    contact = models.CharField(max_length=100)
    live_location = models.CharField(max_length=100)
