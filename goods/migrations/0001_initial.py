# Generated by Django 5.0.3 on 2024-03-14 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='شناسه محصول')),
                ('title', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('status', models.CharField(choices=[('A', 'موجود'), ('N', 'ناموجود')], max_length=1, verbose_name='وضعیت محصول')),
                ('count', models.IntegerField(verbose_name='تعداد')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='شناسه دسته')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی\u200d')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True, verbose_name='وضعیت نمایش')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='goods.category', verbose_name='زیردسته')),
            ],
            options={
                'verbose_name': 'دسته بندی ',
                'verbose_name_plural': 'دسته بندی ها ',
            },
        ),
    ]
