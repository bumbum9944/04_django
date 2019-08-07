from django.db import models

# Create your models here.
class Nono(models.Model):
    kname = models.CharField(max_length=50)
    ename = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    second = models.CharField(max_length=200)
    tag = models.CharField(max_length=200)