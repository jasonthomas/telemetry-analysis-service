# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("jobs", "0025_populate_job_schedule")]

    operations = [
        migrations.AddField(
            model_name="sparkjobrun",
            name="size",
            field=models.IntegerField(
                blank=True,
                help_text="Number of computers used to run the job.",
                null=True,
            ),
        )
    ]
