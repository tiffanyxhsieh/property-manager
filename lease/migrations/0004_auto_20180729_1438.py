# Generated by Django 2.0.5 on 2018-07-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0003_auto_20180729_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='lease',
            name='date_approved',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lease',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
