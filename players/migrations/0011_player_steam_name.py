# Generated by Django 3.1.2 on 2020-11-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_remove_vehicle_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='steam_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
