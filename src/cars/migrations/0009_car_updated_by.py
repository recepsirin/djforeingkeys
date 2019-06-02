# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-05-30 11:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0008_auto_20190530_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_car_user', to=settings.AUTH_USER_MODEL),
        ),
    ]