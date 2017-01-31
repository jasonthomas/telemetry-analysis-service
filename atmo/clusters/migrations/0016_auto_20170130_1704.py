# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-30 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clusters', '0015_auto_20170124_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='emr_release',
            field=models.CharField(choices=[(b'5.2.1', b'5.2.1'), (b'5.0.0', b'5.0.0'), (b'4.5.0', b'4.5.0')], default=b'5.2.1', help_text=b'Different AWS EMR versions have different versions of software like Hadoop, Spark, etc. See <a href="http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html">what\'s new</a> in each.', max_length=50, verbose_name=b'EMR release'),
        ),
    ]