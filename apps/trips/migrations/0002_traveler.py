# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 19:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Traveler_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Trip_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Trip')),
            ],
        ),
    ]
