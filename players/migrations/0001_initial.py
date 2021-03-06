# Generated by Django 3.1.2 on 2020-10-21 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discordName', models.CharField(max_length=200, null=True)),
                ('ingameName', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discordName', models.CharField(max_length=200, null=True)),
                ('ingameName', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('squad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.squad')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donationDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('amount', models.FloatField(null=True)),
                ('note', models.CharField(max_length=200, null=True)),
                ('player', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='players.squad')),
            ],
        ),
    ]
