# Generated by Django 4.2.9 on 2024-01-25 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0002_business_business_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('description', models.TextField()),
            ],
        ),
    ]
