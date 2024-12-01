from django.shortcuts import render
from .models import Taxi


def taxi_list(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        plate = request.GET.get('plate')
        driver = request.GET.get('driver')
        passenger = request.GET.get('passenger')
        model = request.GET.get('model')
        statsu = request.GET.get('statsu')

    if name and plate and driver and passenger and model and statsu:
        Taxi.objects.create(
            name = name,
            plate = plate,
            driver = driver,
            passenger = passenger,
            model = model,
            statsu = statsu,

        )
    taxi = Taxi.objects.all()
    ctx = {'taxi': taxi}
    return render(request, 'taxi/index.html', ctx)