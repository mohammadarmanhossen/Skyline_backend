# Generated by Django 5.2 on 2025-05-28 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_order_booked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='booked',
        ),
    ]
