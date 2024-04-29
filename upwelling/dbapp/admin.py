from django.contrib import admin
from django.conf import settings
from django.utils.html import format_html
from django.utils.dateformat import format
from .models import WellingTable, DateTable, SpatialTable, \
    SourceTable, TerritorialTable, LocationTable, \
    PhysicTable, SpatialCrossTable

@admin.register(DateTable)
class DateTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'start_date',
        'end_date',
        'duration',
        'welling_table'
    )

    fields = [
        ('start_date', 'end_date'),
        'duration',
        'welling_table'
    ]

@admin.register(SpatialTable)
class SpatialTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'strip_length',
        'avg_sea_depth',
        'layer_thickness',
        'welling_table'
    )

    fields = [
        'strip_length',
        'avg_sea_depth',
        'layer_thickness',
        'welling_table'
    ]

@admin.register(SourceTable)
class SourceTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_title',
        'source_url',
        'welling_table'
    )

    fields = [
        'source_title',
        'source_url',
        'welling_table'
    ]

@admin.register(TerritorialTable)
class TerritorialTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'territorial_waters',
        'welling_table'
    )

    fields = [
        'territorrial_waters',
        'welling_table'
    ]

@admin.register(LocationTable)
class LocationTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'reservoir',
        'measurment_place',
        'coordinate_y',
        'latitude',
        'coordinate_x',
        'longitude',
        'welling_table'
    )

    list_filter = (
        'reservoir',
        'measurment_place'
    )

    # fieldsets ????

    fields = [
        'reservoir',
        'measurment_place',
        ('coordinate_y', 'latitude'),
        ('coordinate_x', 'longitude'),
        'welling_table'
    ]

@admin.register(PhysicTable)
class PhysicTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'temperature_diff',
        'temperature_diff_max',
        'flow_speed',
        'seawater_dens_diff',
        'salinity',
        'sea_surf_temp_min',
        'sea_surf_temp_max_diff',
        'wind_speed',
        'vertical_speed',
        'water_temp_max_out',
        'welling_table'
    )

    fields = [
        'temperature_diff',
        'temperature_diff_max',
        'flow_speed',
        'seawater_dens_diff',
        'salinity',
        'sea_surf_temp_min',
        'sea_surf_temp_max_diff',
        'wind_speed',
        'vertical_speed',
        'water_temp_max_out',
        'welling_table'
    ]

@admin.register(SpatialCrossTable)
class SpatialCrossTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'width_on_surface',
        'width_on_bottom',
        'distance_from_shore',
        'welling_table'
    )

    fields = [
        'width_on_surface',
        'width_on_bottom',
        'distance_from_shore',
        'welling_table'
    ]

class DateTableInline(admin.TabularInline):
    model = DateTable

class SpatialTableInline(admin.TabularInline):
    model = SpatialTable

class SourceTableInline(admin.TabularInline):
    model = SourceTable

class TerritorialTableInline(admin.TabularInline):
    model = TerritorialTable

class LocationTableInline(admin.TabularInline):
    model = LocationTable

class PhysicTableInline(admin.TabularInline):
    model = PhysicTable

class SpatialCrossTableInline(admin.TabularInline):
    model = SpatialCrossTable

#class StartDateListFilter(admin.SimpleListFilter):
#    title = "Start date"
#
#    parameter_name = "start_date"
#
#    def lookups(self, request, model_admin):


@admin.register(WellingTable)
class WellingTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type_welling',
        'show_date',
        'show_spatial',
        'show_source',
        'show_location',
        'show_physic',
        'show_spatial_cross',
    )

    list_filter = (
        'type_welling',
    )

    fields = [
        'type_welling'
    ]

    search_fields = [
        'id',
    ]

    inlines = [
        DateTableInline,
        SpatialTableInline,
        SourceTableInline,
        TerritorialTableInline,
        LocationTableInline,
        PhysicTableInline,
        SpatialCrossTableInline
    ]

    def show_date(self, obj):
        result = DateTable.objects.filter(welling_table=obj)[0]

        template = 'Начало замеров: <b>{0}</b><br> \
                Конец замеров: <b>{1}</b><br> \
                Продолжительность: <b>{2}</b> д.'

        return format_html(
                template,
                str(format(result.start_date, settings.DATE_FORMAT)),
                str(format(result.end_date, settings.DATE_FORMAT)),
                str(result.duration)
            )
    show_date.short_description = 'Date'

    def show_spatial(self, obj):
        result = SpatialTable.objects.filter(welling_table=obj)

        if not result:
            return '-'

        result = result[0]

        template = 'Протяженность полосы <b>{0}</b> км<br>\
                Средняя глубина моря <b>{1}</b> м<br>\
                Толщина слоя <b>{2}</b> м'
        
        return format_html(
                template,
                str(result.strip_length),
                str(result.avg_sea_depth),
                str(result.layer_thickness)
            )
    show_spatial.short_description = 'Spatial'

    def show_source(self, obj):
        result = SourceTable.objects.filter(welling_table=obj)[0]

        template = '<a href="{0}">{1}</a>'

        return format_html(
                template,
                result.source_url,
                result.source_title
            )
    show_source.short_description = 'Source'

    def show_location(self, obj):
        result_location = LocationTable.objects.filter(welling_table=obj)[0]
        result_territory = TerritorialTable.objects.filter(welling_table=obj)[0]

        template = 'Страна: <b>{0}</b><br>\
            Водоем: <b>{1}</b><br>\
            Территория: <b>{2}</b><br>\
            Координаты: <b>{3} {4}  {5} {6}</b>'

        return format_html(
                template,
                result_territory.territorial_waters,
                result_location.reservoir,
                result_location.measurment_place,
                str(result_location.coordinate_x),
                result_location.longitude,
                str(result_location.coordinate_y),
                result_location.latitude
            )
    show_location.short_description = 'Location'

    def show_physic(self, obj):
        result = PhysicTable.objects.filter(welling_table=obj)[0]

        template = 'Разница темеператур: <b>{0}</b> °С<br>\
            Макс. перепад темп. между глуб. и пов. водами: <b>{1}</b> °С<br>\
            Скорость течения: <b>{2}</b> м/с<br>\
            Разность плотностей морской воды: <b>{3}</b> епс<br>\
            Соленость: <b>{4}</b> psu<br>\
            Мин. значение темп. пов. воды: <b>{5}</b> °С<br>\
            Макс. перепад темп. пов. воды между зоной явления и смеж. водами: <b>{6}</b> °С<br>\
            Скорость ветра: <b>{7}</b> м/с<br>\
            Вертикальная скорость: <b>{8}</b> м/с<br>\
            Темп. вод. массы за пределами апвеллинга Tmax: <b>{9}</b> °С'
        
        return format_html(
            template,
            str(result.temperature_diff),
            str(result.temperature_diff_max),
            str(result.flow_speed),
            str(result.seawater_dens_diff),
            str(result.salinity),
            str(result.sea_surf_temp_min),
            str(result.sea_surf_temp_max_diff),
            str(result.wind_speed),
            str(result.vertical_speed),
            str(result.water_temp_max_out)
        )
    show_physic.short_description = 'Physic'

    def show_spatial_cross(self, obj):
        result = SpatialCrossTable.objects.filter(welling_table=obj)

        if not result:
            return '-'
        
        result = result[0]

        template = 'Ширина на поверхности: <b>{0}</b> км<br>\
            Ширина у дна: <b>{1}</b> км<br>\
            Расстояние от берега: <b>{2}</b> км'
        
        return format_html(
            template,
            str(result.width_on_surface),
            str(result.width_on_bottom),
            str(result.distance_from_shore)
        )
    show_spatial_cross.short_description = 'Cpatial cross'


# Register your models here.
    
#admin.site.register(WellingTable)
#admin.site.register(DateTable)
#admin.site.register(SpatialTable)
#admin.site.register(SourceTable)
#admin.site.register(TerritorialTable)
#admin.site.register(LocationTable)
#admin.site.register(PhysicTable)
#admin.site.register(SpatialCrossTable)