# Generated by Django 4.2.11 on 2024-06-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0003_alter_vehicle_platenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
    ]