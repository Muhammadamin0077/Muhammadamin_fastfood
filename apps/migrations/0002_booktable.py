# Generated by Django 5.1.4 on 2025-01-07 10:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('telefon', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Telefon raqami '+998' bilan boshlanishi va 9 ta raqamdan iborat bo‘lishi kerak.", regex='^\\+998\\d{9}$')])),
                ('soni', models.IntegerField()),
                ('sana', models.DateField()),
            ],
        ),
    ]
