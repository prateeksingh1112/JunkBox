# Generated by Django 3.0.5 on 2020-06-18 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movi', '0015_auto_20200617_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
