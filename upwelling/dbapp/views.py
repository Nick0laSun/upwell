from django.shortcuts import render
from django.views import generic
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.html import format_html
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
from io import BytesIO
import base64
import json
# from django.shortcuts import renderfrom django-yandex-maps-0.2
# from yandex_maps import api
from .models import WellingTable, TerritorialTable, \
    DateTable, PhysicTable, SourceTable, SpatialTable, \
    LocationTable, SpatialCrossTable
from .forms import SourceForm, StatForm

resevoirs = [{
    "name": "Балтийское море",
    "x": 21.25,
    "y": 59.20},
]

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

    # points_json_dumps = json.dumps({"data": list(points)})

    #points = points[0]
    #for point in points:
    #    print(point)
    # print(points)

    print(points_json)
    return render(request, 'map.html', {"points": points_json})

def points_data(request):
    points = LocationTable.objects.all()
    points_list = []

    for point in points:
        id = point.pk
        x_coord = point.coordinate_x
        y_coord = point.coordinate_y
        resevoir = point.reservoir

        if not x_coord and not y_coord:
            for tic in resevoirs:
                if resevoir == tic['name']:
                    x_coord = tic['x']
                    y_coord = tic['y']
        else:
            if point.longitude == 'W':
                x_coord = -x_coord
        
            if point.latitude == 'S':
                y_coord = -y_coord
        coordinates = [y_coord, x_coord]

        welling = WellingTable.objects.get(pk=point.welling_table.pk)

        head_template = '<a href={% url "detailed_view" {0} %}>{1}</a>'
        body_template = ""

        balloonHeader = 'Upwelling title'#format_html(head_template, point.welling_table.pk, welling)

        balloon_dict = {
            'type': 'Feature',
            'id': id,
            'geometry': {
                'type': 'Point',
                'coordinates': coordinates},
            'properties': {
                'balloonContentHeader': balloonHeader,
                'balloonContentBody': 'Upwelling body',}
        }

        points_list.append(balloon_dict)

        # print('tic')
    
    context = {
        'type': 'FeatureCollection',
        'features': points_list
    }

    
    # return JsonResponse(points, safe=False)
    # return JsonResponse({'foo': 'bar'})
    return JsonResponse(context)

def data_stat(request):
    data = "Нажми на кнопку, получишь результат"
    form = StatForm()

    context = {
        'message': data,
        'form': form
    }
    return render(request, 'data_stat.html', context)

def plot_stat(request):
    data = defaultdict(int)
    recount = WellingTable.objects.all().count()
    form = StatForm()

    font = {'size': 24}
    plt.rc('font', **font)
    plt.rcParams['figure.figsize'] = [15, 10]

    if 'year' in request.GET['stat']:
        values = DateTable.objects.values("start_date")

        plt.xlabel("Год")
        plt.title("Распределение записей по годам")

        for value in values:
            data[value["start_date"].year] += 1
    elif 'season' in request.GET['stat']:
        values = DateTable.objects.values("start_date")

        plt.xlabel("Сезон")
        plt.title("Распределение записей по сезонам")

        for value in values:
            if value["start_date"].month in [12, 1, 2]:
                data["Зима"] += 1
            elif value["start_date"].month in [3, 4, 5]:
                data["Весна"] += 1
            elif value["start_date"].month in [6, 7, 8]:
                data["Лето"] += 1
            else:
                data["Осень"] += 1     
    elif 'month' in request.GET['stat']:
        values = DateTable.objects.values("start_date")

        plt.xlabel("Месяц")
        plt.title("Распределение записей по месяцам")

        for value in values:
            data[value["start_date"].month] += 1

    for k, v in data.items():
        data[k] = v / recount * 100

    # data = {
    #     "лето": 60,
    #     "осень": 20,
    #     "зима": 5,
    #     "весна": 15
    # }

    print(len(list(data.keys())))
    print(data)

    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()))
    plt.yticks(np.arange(0, 100.1, 25.0))
    # plt.xlabel("Сезоны")
    plt.ylabel("Процент от всех записей (%)")
    # plt.title("Распределение записей по сезонам")
    
    # plt.yticks(np.arange(0, max(list(data.values()))+1, 1.0))
    # plt.yaxis.set_major_locator(MaxNLocator(integer=True))

    buffer = BytesIO()
    response = HttpResponse(content_type="image/png")
    plt.savefig(buffer, format="png") #png
    # plt.savefig(response, format="png") #png
    # print(response)
    # return response
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png) #.decode('utf-8')
    graphic = graphic.decode('utf-8') # 'utf-8'
    
    template = '<img src="data:image/png:base64,{0}>"'

    context = {
        'data': data,
        'graphic': graphic,
        # 'img_graph': format_html(
        #     template,
        #     str(graphic)
        # )
        'form': form,
        'response': response
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