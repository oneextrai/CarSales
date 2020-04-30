# Generated by Django 3.0 on 2020-04-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=250)),
                ('year', models.CharField(max_length=5)),
                ('mileage', models.CharField(max_length=10)),
                ('body_style', models.CharField(max_length=50)),
                ('fuel_type', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('photos', models.TextField()),
            ],
        ),
    ]
