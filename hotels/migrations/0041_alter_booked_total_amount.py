# Generated by Django 5.1.3 on 2025-02-13 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0040_remove_booked_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='total_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
