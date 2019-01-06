# Generated by Django 2.1 on 2018-08-26 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20180826_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyweathermodel',
            name='location',
            field=models.ForeignKey(blank=True, help_text='Location this data is relevant for', null=True, on_delete=django.db.models.deletion.CASCADE, to='weather.WeatherConfigurationModel', verbose_name='Location'),
        ),
    ]
