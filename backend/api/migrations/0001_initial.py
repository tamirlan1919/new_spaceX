# Generated by Django 4.2.4 on 2023-08-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=100, verbose_name='Первое поле ')),
                ('second', models.CharField(max_length=100, verbose_name='Второе поле ')),
                ('third', models.CharField(max_length=100, verbose_name='Третье поле ')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255, verbose_name='Элемент списка ')),
            ],
            options={
                'verbose_name': 'Список',
                'verbose_name_plural': 'Список',
            },
        ),
    ]
