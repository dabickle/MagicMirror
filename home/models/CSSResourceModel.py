from django.db import models
from django.utils.translation import gettext as _
from . import Bundle_Path_Max_Length


class CSSResourceModel(models.Model):

    css_file_path = _("Relative to the /static/ endpoint")

    sourcePath = models.CharField(max_length=Bundle_Path_Max_Length,
                                  help_text=css_file_path
                                  )

    def __str__(self):
        return self.sourcePath

    @staticmethod
    def get_manager():
        return CSSResourceModel.objects

    class Meta:
        verbose_name = _("CSS File")
        verbose_name_plural = _("CSS Files")
