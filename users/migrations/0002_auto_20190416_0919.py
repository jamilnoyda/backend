# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-16 09:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(db_index=True,default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]