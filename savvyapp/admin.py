from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Businesses

@admin.register(Businesses)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
