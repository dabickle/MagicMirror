from django.db import models
from django.utils.translation import gettext as _
from . import Free_Text_Max_Length


class DailyWeatherModel(models.Model):

    location = models.ForeignKey(
        "WeatherConfigurationModel",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Location"),
        help_text=_("Location this data is relevant for")
    )

    date = models.DateField(unique=True)
    description = models.CharField(max_length=Free_Text_Max_Length,
                                   blank=True,
                                   null=True
                                   )

    high_temp = models.FloatField(blank=True, null=True)
    main_temp = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    low_temp = models.FloatField(blank=True, null=True)
    snow_amt = models.FloatField(blank=True, null=True)
    rain_amt = models.FloatField(blank=True, null=True)
    wind_speed = models.FloatField(blank=True, null=True)
    wind_direct = models.IntegerField(blank=True, null=True)
    icon_key = models.CharField(
        max_length=Free_Text_Max_Length, blank=True, null=True)
    sunrise = models.TimeField(blank=True, null=True)
    sunset = models.TimeField(blank=True, null=True)

    def __str__(self):
        return "{} : {}".format(
            str(self.location),
            str(self.date)
        )

    @staticmethod
    def get_manager():
        return DailyWeatherModel.objects
