# Generated by Django 2.0.5 on 2018-06-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HousingApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_application_submitted', models.DateTimeField()),
                ('lease_start', models.DateField()),
                ('lease_duration', models.CharField(blank=True, choices=[('6', '6 Months'), ('8', '8 Months'), ('12', '12 Months'), ('15', '15 Months')], default='12', help_text='Lease Duration', max_length=2)),
                ('application_status', models.CharField(choices=[('APPLIED', 'Submitted'), ('IN_REVIEW', 'In review'), ('DENIED', 'Denied'), ('APPROVED', 'Approved')], max_length=15)),
                ('applicants', models.ManyToManyField(to='accounts.Customer')),
            ],
        ),
    ]
