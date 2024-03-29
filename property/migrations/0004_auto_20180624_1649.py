# Generated by Django 2.0.5 on 2018-06-24 16:49

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20180624_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='housing_application',
        ),
        migrations.AddField(
            model_name='property',
            name='state',
            field=localflavor.us.models.USStateField(default='AL', max_length=2),
        ),
        migrations.AddField(
            model_name='property',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='property',
            name='occupied_by',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer'),
        ),
    ]
