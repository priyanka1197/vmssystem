# Generated by Django 3.0.7 on 2020-06-29 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200630_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 30, 7, 43, 52, 774532)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 30, 7, 43, 52, 772530)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2020, 6, 30, 7, 43, 52, 772530)),
        ),
    ]
