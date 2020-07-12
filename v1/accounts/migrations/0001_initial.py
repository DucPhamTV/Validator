# Generated by Django 3.0.6 on 2020-07-06 05:24

import django.core.validators
from django.db import migrations, models
import thenewboston.utils.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('account_number', models.CharField(max_length=64, unique=True)),
                ('balance', models.DecimalField(decimal_places=16, default=0, max_digits=32, validators=[django.core.validators.MinValueValidator(0), thenewboston.utils.validators.validate_is_real_number])),
                ('balance_lock', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'default_related_name': 'accounts',
            },
        ),
    ]
