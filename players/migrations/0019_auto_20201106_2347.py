# Generated by Django 3.1.2 on 2020-11-06 22:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0018_auto_20201105_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='player',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
