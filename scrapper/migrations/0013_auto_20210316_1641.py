# Generated by Django 3.1.5 on 2021-03-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0012_remove_productimages_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producthighlights',
            name='highlight',
            field=models.CharField(blank=True, max_length=2048, null=True),
        ),
    ]
