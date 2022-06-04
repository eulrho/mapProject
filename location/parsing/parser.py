import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from location.models import ParkingLot
import json



def parsing():
    with open('pList.json', encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    post = []

    for i in range(3):
        post.append({
            'name' : json_data['parkinglots'][i]['name'],
            'lat' : json_data['parkinglots'][i]['latitude'],
            'lon': json_data['parkinglots'][i]['longitude'],
            'areaT': json_data['parkinglots'][i]['areatype']
        })

    return post

if __name__ == '__main__':
    post = parsing()

    for i in range(len(post)):
        ParkingLot(
            name = post[i]['name'],
            latitude = post[i]['lat'],
            longitude = post[i]['lon'],
            areatype = post[i]['areaT']
        ).save()
