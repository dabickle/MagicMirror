# Generated by Django 2.1 on 2018-08-26 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180826_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magicmirrorconfigmodel',
            name='height_unit',
            field=models.CharField(choices=[('cm', 'Centimeters'), ('mm', 'Millimeters'), ('in', 'Inches'), ('px', 'Pixels'), ('pt', 'Points'), ('pc', 'Picas'), ('em', 'Relative to font-size'), ('ex', 'Relative to x-height'), ('ch', 'Relative to the "0" character'), ('rem', 'Relative to font size of root element'), ('vm', 'Relative to width of viewport'), ('vh', 'Relative to height of viewport'), ('vmin', 'Min of vm and vh'), ('vmax', 'Max of vm and vh'), ('%', 'Percent')], max_length=100),
        ),
        migrations.AlterField(
            model_name='magicmirrorconfigmodel',
            name='height_value',
            field=models.IntegerField(help_text='Number of whatever column unit desired', verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='magicmirrorconfigmodel',
            name='width_unit',
            field=models.CharField(choices=[('cm', 'Centimeters'), ('mm', 'Millimeters'), ('in', 'Inches'), ('px', 'Pixels'), ('pt', 'Points'), ('pc', 'Picas'), ('em', 'Relative to font-size'), ('ex', 'Relative to x-height'), ('ch', 'Relative to the "0" character'), ('rem', 'Relative to font size of root element'), ('vm', 'Relative to width of viewport'), ('vh', 'Relative to height of viewport'), ('vmin', 'Min of vm and vh'), ('vmax', 'Max of vm and vh'), ('%', 'Percent')], max_length=10),
        ),
    ]
