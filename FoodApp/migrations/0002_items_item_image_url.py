# Generated by Django 5.0.6 on 2024-07-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='item_image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
