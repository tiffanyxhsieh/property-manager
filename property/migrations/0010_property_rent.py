# Generated by Django 2.0.5 on 2018-07-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_remove_property_occupied_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rent',
            field=models.IntegerField(default=1000),
        ),
    ]
