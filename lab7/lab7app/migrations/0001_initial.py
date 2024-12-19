# Generated by Django 5.1.4 on 2024-12-19 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('license_number', models.CharField(max_length=255, unique=True)),
                ('birth_date', models.DateField()),
                ('driving_experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('manufacture_year', models.IntegerField()),
                ('registration_number', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleAssignment',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('assignment_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab7app.driver')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab7app.vehicle')),
            ],
        ),
    ]
