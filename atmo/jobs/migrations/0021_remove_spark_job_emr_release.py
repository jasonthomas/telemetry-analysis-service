# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-21 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_alter_spark_job_emr_release'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sparkjob',
            name='emr_release_version',
        ),
    ]