# Generated by Django 5.1.4 on 2025-01-12 01:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_car_delete_product_alter_student_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='car',
            name='model',
        ),
        migrations.RemoveField(
            model_name='car',
            name='year',
        ),
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 12, 1, 49, 11, 579080)),
        ),
    ]
