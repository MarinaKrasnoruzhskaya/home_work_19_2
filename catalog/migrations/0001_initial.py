# Generated by Django 5.0.6 on 2024-07-03 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название категории', max_length=100, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название продукта', max_length=100, verbose_name='Название продукта')),
                ('description', models.TextField(blank=True, help_text='Введите описание продукта', null=True, verbose_name='Описание продукта')),
                ('preview', models.ImageField(blank=True, help_text='Загрузите изображение продукта', null=True, upload_to='products/', verbose_name='Изображение')),
                ('price', models.IntegerField(help_text='Введите цену за покупку', verbose_name='Цена за покупку')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(blank=True, help_text='Введите категорию продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
