# Generated by Django 3.1.2 on 2020-11-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0015_remove_case_case_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]