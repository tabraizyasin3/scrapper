# Generated by Django 3.2.4 on 2022-01-24 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0033_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpagesscrapper',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scrapper.categories'),
        ),
    ]