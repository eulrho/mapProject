import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from django.shortcuts import render
from location.models import ParkingLot

def parkingLot(request):
    parkinglots = ParkingLot.objects.all
    context = {'parkinglots':parkinglots}
    return render(request, 'location/default.html', context)