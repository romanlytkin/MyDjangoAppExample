from django.db import models

class Region(models.Model):
    region_name = models.CharField(max_length=80)

class City(models.Model):
    city_name = models.CharField(max_length=80)

class RegionCity(models.Model):
    region = models.ForeignKey(Region)
    city = models.ForeignKey(City)

class Comments(models.Model):
    fname = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    lname = models.CharField(max_length=80)
    region = models.ForeignKey(Region)
    city = models.ForeignKey(City)
    phone = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    comment = models.CharField(max_length=160)
