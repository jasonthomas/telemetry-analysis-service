# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0041_auto_20170530_1857'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='sparkjobrunalert',
            index_together=set([('reason_code', 'mail_sent_date')]),
        ),
    ]
