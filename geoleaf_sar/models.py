from django.contrib.gis.db import models

# Create your models here.


class Species(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=100)