from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upwellings/', views.UpwellingListView.as_view(), name='upwellings'),
    path('map_test/', views.default_map, name="default"),
]