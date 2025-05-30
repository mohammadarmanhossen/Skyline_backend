# Generated by Django 5.2 on 2025-05-28 02:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0053_delete_order'),
        ('payment', '0009_remove_order_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='booked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='hotels.booked'),
        ),
    ]
