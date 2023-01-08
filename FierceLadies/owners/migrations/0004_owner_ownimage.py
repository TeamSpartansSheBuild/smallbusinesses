# Generated by Django 4.1.3 on 2023-01-08 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0003_owner_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='ownImage',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='owner_images'),
        ),
    ]