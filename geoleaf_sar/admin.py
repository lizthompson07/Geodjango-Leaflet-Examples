from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Species

@admin.register(Species)
class SpeciesAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')



