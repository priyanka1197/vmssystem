# Generated by Django 2.2.7 on 2020-06-25 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='hostname',
            field=models.CharField(default='Admin', max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='adharcard',
            field=models.ImageField(null=True, upload_to='img/adhar'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='image',
            field=models.ImageField(upload_to='img/image'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='license',
            field=models.ImageField(null=True, upload_to='img/license'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='licenseno',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='pancard',
            field=models.ImageField(null=True, upload_to='img/pan'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='pancardno',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 6, 25, 13, 34, 47, 537961)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 6, 25, 13, 34, 47, 537369)),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2020, 6, 25, 13, 34, 47, 537480)),
        ),
    ]
