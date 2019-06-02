# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-05-30 10:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0003_auto_20190530_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='first_owner',
        ),
        migrations.AddField(
            model_name='car',
            name='passengers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]