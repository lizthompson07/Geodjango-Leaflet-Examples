from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Species

latitude = 49.042504
longitude = -63.718084

user_location = Point(longitude, latitude, srid=4326)

# Create your views here.


class Home(generic.ListView):
    model = Species
    context_object_name = "species"
    queryset = Species.objects.annotate(distance=Distance("location", user_location)).order_by("distance")[0:6]
    template_name = "geoleaf_sar/index.html"