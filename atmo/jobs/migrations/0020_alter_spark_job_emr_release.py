# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-21 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("jobs", "0019_convert_spark_job_emr_release")]

    operations = [
        migrations.AlterField(
            model_name="sparkjob",
            name="emr_release",
            field=models.ForeignKey(
                help_text='Different AWS EMR versions have different versions of software like Hadoop, Spark, etc. See <a href="http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html">what\'s new</a> in each.',
                on_delete=django.db.models.deletion.PROTECT,
                related_name="created_sparkjobs",
                to="clusters.EMRRelease",
                verbose_name="EMR release",
            ),
        )
    ]
