from django.urls import path, re_path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.default_map, name="map"),
    #path('sources/', views.SourceListView.as_view(), name='sources'),
    path('sources/', views.source_list, name='sources'),
    path('data_stat/', views.data_stat, name='data_stat'),
    re_path('points_data/', views.points_data, name='points_data'),
    re_path(r'^data_stat/plot/', views.plot_stat, name='plot'), # [-\w]+ (?P<stat>\w+)
    #re_path(r'^search/(?P<search_field>.*)$', views.source_search, name='source_search'),
    re_path('search/', views.source_search, name='source_search'),
    re_path(r'^sources/upwelling_record/(?P<id>\d+)/view$', views.detailed_view, name='detailed_view'),
]