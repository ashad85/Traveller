# Generated by Django 4.2.1 on 2023-11-30 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='user1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='trip_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Date_of_birth', models.DateField()),
                ('Phone_number', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=100)),
                ('Address', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=50)),
                ('Zip_code', models.CharField(max_length=20)),
                ('Document', models.CharField(max_length=20)),
                ('Document_number', models.CharField(max_length=50)),
                ('Holiday_place', models.CharField(max_length=50)),
                ('Child', models.IntegerField(default=0)),
                ('Adult', models.IntegerField(default=0)),
                ('Old', models.IntegerField(default=0)),
                ('Guest', models.TextField()),
                ('Guest_Doc_number', models.TextField()),
                ('Check_in', models.DateField()),
                ('Check_out', models.DateField()),
                ('Meal', models.CharField(max_length=10)),
                ('Star', models.IntegerField(default=1)),
                ('Mount', models.CharField(max_length=50)),
                ('Mount_number', models.IntegerField()),
                ('Bungy', models.CharField(max_length=50)),
                ('Bungy_number', models.IntegerField()),
                ('River', models.CharField(max_length=50)),
                ('River_number', models.IntegerField()),
                ('Cab', models.CharField(max_length=10)),
                ('Picklocation', models.CharField(max_length=150)),
                ('Droplocation', models.CharField(max_length=150)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]