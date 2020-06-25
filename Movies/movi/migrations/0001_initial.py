# Generated by Django 3.0.5 on 2020-06-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('Movie_name', models.CharField(default=' ', max_length=50)),
                ('year', models.CharField(default=' ', max_length=20)),
                ('link', models.CharField(default=' ', max_length=20)),
                ('image', models.CharField(default=' ', max_length=20)),
            ],
        ),
    ]