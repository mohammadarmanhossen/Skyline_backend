# Generated by Django 5.2 on 2025-04-30 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
    ]
