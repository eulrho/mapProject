from django.contrib import admin
from .models import ParkingLot

class ParkingLotAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(ParkingLot, ParkingLotAdmin)