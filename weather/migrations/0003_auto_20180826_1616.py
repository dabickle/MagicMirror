# Generated by Django 2.1 on 2018-08-26 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_weatherconfigurationmodel_weatherconfigurationuserbridge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherconfigurationuserbridge',
            old_name='app',
            new_name='weatherConfiguration',
        ),
    ]
