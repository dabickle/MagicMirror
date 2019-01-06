# Generated by Django 2.1 on 2018-10-17 04:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0013_auto_20181016_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationmodel',
            name='uniqueId',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Unique ID'),
        ),
    ]
