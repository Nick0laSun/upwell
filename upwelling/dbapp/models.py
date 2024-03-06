from django.db import models

# Create your models here.

class WellingTable(models.Model):
    type_welling = models.CharField(max_length=45)

class DateTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()

class SpatialTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE)
    strip_length = models.FloatField()
    avg_sea_depth = models.FloatField()
    layer_thickness = models.FloatField()

class SourceTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE)
    source_title = models.CharField(max_length=1000)
    source_url = models.CharField(max_length=512)

class TerritorialTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE)
    territorial_waters = models.CharField(max_length=45)

class LocationTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE)
    reservoir = models.CharField(max_length=45)
    measurment_place = models.CharField(max_length=225)
    coordinate_y = models.FloatField()
    latitude = models.CharField(max_length=1)
    coordinate_x = models.FloatField()
    longitude = models.CharField(max_length=1)

class PhysicTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE)
    temperature_diff = models.FloatField()
    temperature_diff_max = models.FloatField()
    flow_speed = models.FloatField()
    seawater_dens_diff = models.FloatField()
    salinity = models.FloatField()
    sea_surf_temp_min = models.FloatField()
    sea_surf_temp_max_diff = models.FloatField()
    wind_speed = models.FloatField()
    vertical_speed = models.FloatField()
    water_temp_max_out = models.FloatField()

class SpatialCrossTable(models.Model):
    welling_table = models.ForeignKey(WellingTable, on_delete=models.CASCADE)
    width_on_surface = models.FloatField()
    width_on_bottom = models.FloatField()
    distance_from_shore = models.FloatField()