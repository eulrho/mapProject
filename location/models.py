from django.db import models

class ParkingLot(models.Model):
    CHOICE = (
        ('E', 'E구역'), ('N', 'N구역'), ('S', 'S구역'), ('etc', '기타')
    )
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    areatype = models.CharField(max_length=200, choices=CHOICE, default='E')

class Filter(models.Model):
    E = models.BooleanField(default='True')
    N = models.BooleanField(default='True')
    S = models.BooleanField(default='True')