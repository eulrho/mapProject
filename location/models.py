from django.db import models

class ParkingLot(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    areatype = models.CharField(max_length=200)
