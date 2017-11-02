# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-02 18:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('editor', '0011_chapter_checked_statuses'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='assigned',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
