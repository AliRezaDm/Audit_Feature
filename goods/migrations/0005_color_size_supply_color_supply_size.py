# Generated by Django 5.0.3 on 2024-03-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_supply_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='نام رنگ')),
            ],
            options={
                'verbose_name': 'رنگ',
                'verbose_name_plural': 'رنگ ها',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='عنوان اندازه')),
            ],
            options={
                'verbose_name': 'اندازه',
                'verbose_name_plural': 'اندازه ها',
            },
        ),
        migrations.AddField(
            model_name='supply',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, related_name='goods', to='goods.color', verbose_name='رنگ'),
        ),
        migrations.AddField(
            model_name='supply',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, related_name='goods', to='goods.size', verbose_name='اندازه'),
        ),
    ]