# Generated by Django 5.1.3 on 2025-01-01 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0020_review_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel'),
        ),
    ]
