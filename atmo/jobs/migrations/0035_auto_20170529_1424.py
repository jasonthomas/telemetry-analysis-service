# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("jobs", "0034_auto_20170529_1424")]

    operations = [
        migrations.AlterModelOptions(
            name="sparkjobrun",
            options={"get_latest_by": "created_at", "ordering": ["-created_at"]},
        )
    ]
