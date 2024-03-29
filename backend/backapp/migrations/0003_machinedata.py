# Generated by Django 5.0.2 on 2024-03-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0002_alter_machine_historical_peak_usage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=50)),
                ('base_power_consumption', models.IntegerField()),
                ('production_rate', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
