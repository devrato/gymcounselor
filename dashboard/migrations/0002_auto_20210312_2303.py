# Generated by Django 3.1.4 on 2021-03-12 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 11, 23, 3, 32, 80737)),
        ),
        migrations.AlterField(
            model_name='order',
            name='oder_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 23, 3, 32, 80737)),
        ),
    ]