# Generated by Django 5.1.4 on 2025-01-12 01:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_car_created_at_remove_car_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 12, 1, 49, 33, 846456, tzinfo=datetime.timezone.utc)),
        ),
    ]
