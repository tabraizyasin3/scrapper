# Generated by Django 3.1.5 on 2021-05-18 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0015_variationsettings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variationsettings',
            old_name='dimension_val',
            new_name='dimension_val_en',
        ),
    ]
