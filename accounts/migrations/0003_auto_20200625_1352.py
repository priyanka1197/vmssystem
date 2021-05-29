# Generated by Django 2.2.7 on 2020-06-25 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200625_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='image',
            field=models.ImageField(null=True, upload_to='img/image'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 25, 13, 52, 19, 600313)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 25, 13, 52, 19, 599801)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2020, 6, 25, 13, 52, 19, 599826)),
        ),
    ]