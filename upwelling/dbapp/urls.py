from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.default_map, name="map"),
    #path('sources/', views.SourceListView.as_view(), name='sources'),
    path('sources/', views.source_list, name='sources'),
    path('data_stat/', views.data_stat, name='data_stat'),
    url('plot_stat/', views.plot_stat, name='plot_stat'),
    #url(r'^search/(?P<search_field>.*)$', views.source_search, name='source_search'),
    url('search/', views.source_search, name='source_search'),
    url(r'^sources/upwelling_record/(?P<id>\d+)/view$', views.detailed_view, name='detailed_view'),
]