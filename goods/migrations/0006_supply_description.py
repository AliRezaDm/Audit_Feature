# Generated by Django 5.0.3 on 2024-04-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_color_size_supply_color_supply_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحی درباره محصول'),
        ),
    ]