# Generated by Django 5.1.6 on 2025-02-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0028_remove_hotel_image_hotel_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booked',
            name='payment',
        ),
        migrations.AddField(
            model_name='booked',
            name='total_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
