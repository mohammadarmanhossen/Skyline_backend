# Generated by Django 5.1.3 on 2025-02-13 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0030_booked_is_paid_booked_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='is_paid',
        ),
        migrations.RemoveField(
            model_name='booked',
            name='status',
        ),
    ]
