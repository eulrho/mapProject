import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()

from django.shortcuts import render, get_object_or_404, redirect
from location.models import ParkingLot, Filter
from location.forms import ParkingLotForm

def parkingLot(request):
    parkinglots = ParkingLot.objects.all()    # 주차장 객체 불러오기

    # 아직 Filter 모델의 객체가 생성되어 있지 않은 경우 객체 생성
    if Filter.objects.count() == 0:
        Filter.objects.create()
    option = get_object_or_404(Filter)     # filter 객체 불러오기. 없다면 error 처리.

    # POST 요청 시
    if request.method == 'POST':
        form = ParkingLotForm(request.POST, instance=option)
        if form.is_valid():    # form 유효성 검사
            option=form.save(commit=False)    # False : DB에 바로 저장되는 것 방지(데이터 추가 후 저장, save 호출 지연)
            option.save()
            return redirect(parkingLot)
    # GET 요청 시
    else:
        form = ParkingLotForm()
    # 체크박스에서 선택되지 않은 데이터 제외
    if option.E == False:
        parkinglots = parkinglots.exclude(areatype='E')
    if option.N == False:
        parkinglots = parkinglots.exclude(areatype='N')
    if option.S == False:
        parkinglots = parkinglots.exclude(areatype='S')

    context = {'parkinglots': parkinglots, 'form':form}
    return render(request, 'location/default.html', context)