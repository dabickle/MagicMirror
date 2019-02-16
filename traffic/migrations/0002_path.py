# Generated by Django 2.1 on 2018-09-09 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PathName', models.CharField(help_text='Friendly name to refer to this UI configuration.', max_length=200)),
                ('EndingLocation', models.ForeignKey(help_text='Ending position of the path', on_delete=django.db.models.deletion.CASCADE, related_name='ending_locations', to='traffic.LocationModel', verbose_name='End Location')),
                ('StartingLocation', models.ForeignKey(help_text='Starting position of the path', on_delete=django.db.models.deletion.CASCADE, related_name='starting_locations', to='traffic.LocationModel', verbose_name='Start Location')),
            ],
        ),
    ]