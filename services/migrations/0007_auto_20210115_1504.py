# Generated by Django 3.1.4 on 2021-01-15 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20210115_1459'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='img_main',
            new_name='img_card',
        ),
    ]
