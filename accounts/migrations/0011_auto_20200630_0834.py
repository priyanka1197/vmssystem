# Generated by Django 3.0.7 on 2020-06-29 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200630_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 30, 8, 34, 33, 779134)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 30, 8, 34, 33, 777132)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2020, 6, 30, 8, 34, 33, 777132)),
        ),
    ]