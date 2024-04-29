from django.shortcuts import render
from django.views import generic
# from django.shortcuts import renderfrom django-yandex-maps-0.2
# from yandex_maps import api
from .models import WellingTable, TerritorialTable, \
    DateTable, PhysicTable, SourceTable, SpatialTable, \
    LocationTable, SpatialCrossTable

# Create your views here.

class UpwellingListView(generic.ListView):
    model = WellingTable

def index(request):

    num_upwelling = WellingTable.objects.all().count()

    return render(
        request,
        'index.html',
        context= {
            'num_upwelling': num_upwelling,
        }
    )


def default_map(request):
    points = LocationTable.objects.values()

    #for point in points:
    #    print(point)
    # print(points)
    return render(request, 'map.html', {"points": points})