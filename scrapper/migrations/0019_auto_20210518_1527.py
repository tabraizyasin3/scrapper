# Generated by Django 3.1.5 on 2021-05-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0018_totalvariations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalvariations',
            name='value_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='totalvariations',
            name='value_en',
            field=models.TextField(blank=True, null=True),
        ),
    ]
