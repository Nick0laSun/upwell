from django.contrib import admin
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

@admin.register(WellingTable)
class WellingTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type_welling'
    )

    list_filter = (
        'type_welling',
    )

    fields = [
        'type_welling'
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

# Register your models here.
    
#admin.site.register(WellingTable)
#admin.site.register(DateTable)
#admin.site.register(SpatialTable)
#admin.site.register(SourceTable)
#admin.site.register(TerritorialTable)
#admin.site.register(LocationTable)
#admin.site.register(PhysicTable)
#admin.site.register(SpatialCrossTable)