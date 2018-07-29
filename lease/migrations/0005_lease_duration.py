# Generated by Django 2.0.5 on 2018-07-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0004_auto_20180729_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='lease',
            name='duration',
            field=models.IntegerField(choices=[(6, '6 Months'), (8, '8 Months'), (12, '12 Months'), (15, '15 Months')], default=6),
        ),
    ]