# Generated by Django 2.0.5 on 2018-07-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180627_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id_number',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='ss_number',
        ),
        migrations.AddField(
            model_name='customer',
            name='ss_number',
            field=models.IntegerField(default=1),
        ),
    ]
