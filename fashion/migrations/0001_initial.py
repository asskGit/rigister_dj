# Generated by Django 5.0.1 on 2024-02-03 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sweatshirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=80)),
                ('brand', models.CharField(max_length=80)),
                ('color', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='sweatshirt/')),
            ],
            options={
                'db_table': 'sweatshirt',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='sweatshirt/')),
                ('sweatshirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fashion.sweatshirt')),
            ],
            options={
                'db_table': 'photo',
            },
        ),
    ]
