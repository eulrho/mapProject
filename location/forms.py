from django import forms
from location.models import Filter

class ParkingLotForm(forms.ModelForm):
    class Meta:
        model = Filter
        fields = '__all__'