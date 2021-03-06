# Generated by Django 3.0 on 2019-12-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StationArrival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_datetime', models.DateTimeField()),
                ('station_name', models.CharField(max_length=100)),
                ('station_abbr', models.CharField(max_length=30)),
                ('destination_name', models.CharField(max_length=100)),
                ('destination_abbr', models.CharField(max_length=30)),
                ('arrival_minutes', models.CharField(max_length=30)),
                ('arrival_datetime', models.DateTimeField()),
                ('platform', models.CharField(max_length=30)),
                ('direction', models.CharField(max_length=30)),
                ('length', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('hexcolor', models.CharField(max_length=30)),
                ('bikeflag', models.CharField(max_length=30)),
                ('delay_seconds', models.IntegerField()),
            ],
        ),
    ]
