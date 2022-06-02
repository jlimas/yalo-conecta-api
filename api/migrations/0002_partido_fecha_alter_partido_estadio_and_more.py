# Generated by Django 4.0.5 on 2022-06-01 22:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='partido',
            name='estadio',
            field=models.CharField(choices=[('Estadio Nacional #1', 'Estadio Nacional #1'), ('Estadio Nacional #2', 'Estadio Nacional #2'), ('Estadio Nacional #3', 'Estadio Nacional #3')], max_length=100),
        ),
        migrations.AlterField(
            model_name='partido',
            name='local',
            field=models.CharField(choices=[('Mexico', 'Mexico'), ('Guatemala', 'Guatemala'), ('Estados Unidos', 'Estados Unidos'), ('Canada', 'Canada')], max_length=100),
        ),
        migrations.AlterField(
            model_name='partido',
            name='visitante',
            field=models.CharField(choices=[('Mexico', 'Mexico'), ('Guatemala', 'Guatemala'), ('Estados Unidos', 'Estados Unidos'), ('Canada', 'Canada')], max_length=100),
        ),
    ]
