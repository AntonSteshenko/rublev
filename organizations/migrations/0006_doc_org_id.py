# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_doc'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='org_id',
            field=models.ForeignKey(default='neit', on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
            preserve_default=False,
        ),
    ]
