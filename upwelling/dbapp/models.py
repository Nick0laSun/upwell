from django.db import models


# Create your models here.

class WellingTable(models.Model):
    type_welling = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="Welling type")

class DateTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE, verbose_name="WellingTableFK")
    start_date = models.DateField(null=True, blank=True, default=None, verbose_name="Start date")
    end_date = models.DateField(null=True, blank=True, default=None, verbose_name="End date")
    duration = models.IntegerField(null=True, blank=True, default=None, verbose_name="Duration of observation")

class SpatialTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE, verbose_name="WellingTableFK")
    strip_length = models.FloatField(null=True, blank=True, default=None, verbose_name="Strip length")
    avg_sea_depth = models.FloatField(null=True, blank=True, default=None, verbose_name="Avg sea depth")
    layer_thickness = models.FloatField(null=True, blank=True, default=None, verbose_name="Layer thickness")

class SourceTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE, verbose_name="WellingTableFK")
    source_title = models.CharField(max_length=1000, null=True, blank=True, default=None, verbose_name="Source title")
    source_url = models.CharField(max_length=512, null=True, blank=True, default=None, verbose_name="Source URL")

class TerritorialTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE, verbose_name="WellingTableFK")
    territorial_waters = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="Territorial waters")

class LocationTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE, verbose_name="WellingTableFK")
    reservoir = models.CharField(max_length=45, null=True, blank=True, default=None, verbose_name="Reservoir")
    measurment_place = models.CharField(max_length=225, null=True, blank=True, default=None, verbose_name="Measurment place")
    coordinate_y = models.FloatField(null=True, blank=True, default=None, verbose_name="Coordinate Y")
    latitude = models.CharField(max_length=1, null=True, blank=True, default=None, verbose_name="Latitude")
    coordinate_x = models.FloatField(null=True, blank=True, default=None, verbose_name="Coordinate X")
    longitude = models.CharField(max_length=1, null=True, blank=True, default=None, verbose_name="Longitude")

class PhysicTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE, verbose_name="WellingTableFK")
    temperature_diff = models.FloatField(null=True, blank=True, default=None, verbose_name="Temperature diff")
    temperature_diff_max = models.FloatField(null=True, blank=True, default=None, verbose_name="Temparature diff max")
    flow_speed = models.FloatField(null=True, blank=True, default=None, verbose_name="Flow speed")
    seawater_dens_diff = models.FloatField(null=True, blank=True, default=None, verbose_name="Seawater dens diff")
    salinity = models.FloatField(null=True, blank=True, default=None, verbose_name="Salinity")
    sea_surf_temp_min = models.FloatField(null=True, blank=True, default=None, verbose_name="Sea surf temp min")
    sea_surf_temp_max_diff = models.FloatField(null=True, blank=True, default=None, verbose_name="Sea surf temp max diff")
    wind_speed = models.FloatField(null=True, blank=True, default=None, verbose_name="Wind speed")
    vertical_speed = models.FloatField(null=True, blank=True, default=None, verbose_name="Vertical speed")
    water_temp_max_out = models.FloatField(null=True, blank=True, default=None, verbose_name="Water temp max out")

class SpatialCrossTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE, verbose_name="WellingTableFK")
    width_on_surface = models.FloatField(null=True, blank=True, default=None, verbose_name="Width on surface")
    width_on_bottom = models.FloatField(null=True, blank=True, default=None, verbose_name="Width on bottom")
    distance_from_shore = models.FloatField(null=True, blank=True, default=None, verbose_name="Distance from shore")