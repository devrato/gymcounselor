# Generated by Django 3.1.4 on 2021-03-14 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210314_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 13, 15, 48, 3, 708563)),
        ),
        migrations.AlterField(
            model_name='order',
            name='oder_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 14, 15, 48, 3, 708563)),
        ),
    ]