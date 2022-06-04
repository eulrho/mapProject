from django import forms
from location.models import ParkingLot

class ParkingLotForm(forms.ModelForm):
    class Meta:
        model = ParkingLot
        fields = ['areatype']