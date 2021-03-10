# Generated by Django 3.1.7 on 2021-02-21 15:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Lakewood', 'Lakewood'), ('Bridgewood', 'Bridgewood'), ('Ridgewood', 'Ridgewood')], default='Lakewood', max_length=30, unique=True)),
                ('classification', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='CustomerFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.CharField(choices=[('Reward', 'Reward'), ('Regular', 'Regular')], default='Regular', max_length=10)),
                ('weekday_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('weekend_rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('hotel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel', verbose_name='customer_fee')),
            ],
            options={
                'unique_together': {('hotel', 'client_type')},
            },
        ),
    ]
