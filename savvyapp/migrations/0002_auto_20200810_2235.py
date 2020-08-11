# Generated by Django 3.0.8 on 2020-08-10 19:35

from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'data.json'
def load_data(apps, schema_editor):
    Businesses = apps.get_model('savvyapp', 'Businesses')
    jsonfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(jsonfile)) as datafile:
        objects = json.load(datafile)
        for obj in objects['elements']:
            try:
                objType = obj['type']
                if objType == 'node':
                    tags = obj['tags']
                    name = tags.get('name','no-name')
                    longitude = obj.get('lon', 0)
                    latitude = obj.get('lat', 0)
                    location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                    Businesses(name=name, location = location).save()
            except KeyError:
                pass

class Migration(migrations.Migration):

    dependencies = [
        ('savvyapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
