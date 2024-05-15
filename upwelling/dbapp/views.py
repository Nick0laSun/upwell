from django.shortcuts import render
from django.views import generic
from django.core import serializers
from collections import defaultdict
# from django.shortcuts import renderfrom django-yandex-maps-0.2
# from yandex_maps import api
from .models import WellingTable, TerritorialTable, \
    DateTable, PhysicTable, SourceTable, SpatialTable, \
    LocationTable, SpatialCrossTable
from .forms import SourceForm

# Create your views here.

class SourceListView(generic.ListView):
    model = SourceTable
    context_object_name = 'source_list'
    template_name = 'source_list.html'

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
    #points = LocationTable.objects.values()
    #points = list(points)
    points = LocationTable.objects.all()
    points_json = serializers.serialize('json', points)

    #points = points[0]
    #for point in points:
    #    print(point)
    # print(points)

    print(points_json)
    return render(request, 'map.html', {"points": points_json})

def data_stat(request):
    data = "Нажми на кнопку, получишь результат"
    context = {
        'data': data
    }
    return render(request, 'data_stat.html', context)

def plot_stat(request):
    data = defaultdict(int)

    if 'year_stat' in request.GET:
        values = DateTable.objects.values("start_date")
        debug = values
        for value in values:
            data[value["start_date"].year] += 1
    elif 'season_stat' in request.GET:
        values = DateTable.objects.values("start_date")
        debug = values
        for value in values:
            if value["start_date"].month in [12, 1, 2]:
                data["Winter"] += 1
            elif value["start_date"].month in [3, 4, 5]:
                data["Spring"] += 1
            elif value["start_date"].month in [6, 7, 8]:
                data["Summer"] += 1
            else:
                data["Fall"] += 1     
    elif 'month_stat' in request.GET:
        values = DateTable.objects.values("start_date")
        debug = values
        for value in values:
            data[value["start_date"].month] += 1

    context = {
        'data': data,
        'debug': debug
    }    
    return render(request, 'data_stat.html', context)

def source_list(request):
    source_list = SourceTable.objects.all()
    form = SourceForm()
    contex = {
        'source_list': source_list,
        'form': form
    }

    return render(request, 'source_list.html', contex)


def source_search(request):
    #source_list = SourceTable.objects.all()

    exp = request.GET['search_field']

    if exp == "all":
        source_list = SourceTable.objects.all()
    else:

        source_list = SourceTable.objects.filter(
            source_title__icontains=exp
        )

    
    form = SourceForm()
    contex = {
        'source_list': source_list,
        'form': form
    }

    return render(request, 'source_list.html', contex)

def detailed_view(request, id):
    welling = WellingTable.objects.values().filter(id=id)[0]
    date = DateTable.objects.values().filter(welling_table=id)[0]
    spatial = SpatialTable.objects.values().filter(welling_table=id)[0]
    source = SourceTable.objects.values().filter(welling_table=id)[0]
    territory = TerritorialTable.objects.values().filter(welling_table=id)[0]
    location = LocationTable.objects.values().filter(welling_table=id)[0]
    physic = PhysicTable.objects.values().filter(welling_table=id)[0]
    spatial_cross = SpatialCrossTable.objects.values().filter(welling_table=id)[0]

    context = {
        'welling': welling,
        'date': date,
        'spatial': spatial,
        'source': source,
        'territory': territory,
        'location': location,
        'physic': physic,
        'spatial_cross': spatial_cross
    }

    # print(context)
    return render(request, 'detailed_view.html', context)