# Generated by Django 5.2 on 2025-05-27 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0053_delete_order'),
        ('payment', '0007_remove_checkout_order_checkout_is_canceled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='booked',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='hotels.booked'),
        ),
    ]
