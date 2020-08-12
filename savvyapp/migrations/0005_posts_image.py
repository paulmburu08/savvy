# Generated by Django 3.0.8 on 2020-08-12 12:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savvyapp', '0004_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=cloudinary.models.CloudinaryField(default='image.png', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
