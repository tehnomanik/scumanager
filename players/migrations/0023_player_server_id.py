# Generated by Django 3.1.3 on 2020-11-07 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0022_auto_20201107_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='server_id',
            field=models.IntegerField(default=0),
        ),
    ]
