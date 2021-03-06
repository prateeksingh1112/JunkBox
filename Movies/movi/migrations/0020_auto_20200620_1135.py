# Generated by Django 3.0.5 on 2020-06-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movi', '0019_auto_20200619_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='awards',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='series',
            name='boxoffice',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='series',
            name='cast',
            field=models.CharField(default=' ', max_length=100000000),
        ),
        migrations.AddField(
            model_name='series',
            name='desc',
            field=models.CharField(default=' ', max_length=100000000),
        ),
        migrations.AddField(
            model_name='series',
            name='director',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='series',
            name='genres',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='series',
            name='image',
            field=models.CharField(default=' ', max_length=100000000),
        ),
        migrations.AddField(
            model_name='series',
            name='language',
            field=models.CharField(default=' ', max_length=10000),
        ),
        migrations.AddField(
            model_name='series',
            name='poster',
            field=models.CharField(default=' ', max_length=10000000),
        ),
        migrations.AddField(
            model_name='series',
            name='rating',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='series',
            name='release_date',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='series',
            name='trailer',
            field=models.CharField(default=' ', max_length=10000000),
        ),
        migrations.AddField(
            model_name='series',
            name='type',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='series',
            name='writer',
            field=models.CharField(default=' ', max_length=1000),
        ),
        migrations.AddField(
            model_name='series',
            name='year',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
