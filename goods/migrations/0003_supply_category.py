# Generated by Django 5.0.3 on 2024-03-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='supply',
            name='category',
            field=models.ManyToManyField(related_name='cat', to='goods.category', verbose_name='دسته بندی'),
        ),
    ]
