from django.urls import path
from location import views

urlpatterns = [
    path('', views.parkingLot),
]