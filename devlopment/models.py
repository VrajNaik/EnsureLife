from django.db import models

# Create your models here.
class Devlopment_team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    img = models.ImageField(upload_to='assets/images')
    fb =models.CharField(max_length=200)
    twitter =models.CharField(max_length=200)
    google =models.CharField(max_length=200)
    pintrest =models.CharField(max_length=200)