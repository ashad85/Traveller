# Generated by Django 4.2.1 on 2023-12-02 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traveller_app', '0006_alter_trip_data_bungy_alter_trip_data_cab_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip_data',
            name='user',
        ),
    ]