# Generated by Django 3.1.4 on 2021-02-02 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('razorpay_payment_id', models.CharField(max_length=50)),
                ('service_name', models.CharField(max_length=50)),
                ('customer_email', models.CharField(max_length=50)),
                ('oder_date', models.DateTimeField(default=datetime.datetime(2021, 3, 4, 22, 15, 48, 385008))),
                ('expiry_date', models.DateTimeField(default=datetime.datetime(2021, 3, 4, 22, 15, 48, 385008))),
            ],
        ),
    ]