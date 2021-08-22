# Generated by Django 3.1.5 on 2021-05-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper', '0019_auto_20210518_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='fc_grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, max_length=60, null=True)),
                ('cond', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.CharField(blank=True, max_length=1500, null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('grade_ar', models.TextField(blank=True, null=True)),
                ('cond_ar', models.TextField(blank=True, null=True)),
                ('description_ar', models.TextField(blank=True, null=True)),
                ('grade_code', models.CharField(blank=True, max_length=384, null=True)),
                ('google_grade', models.CharField(blank=True, max_length=765, null=True)),
            ],
        ),
    ]
