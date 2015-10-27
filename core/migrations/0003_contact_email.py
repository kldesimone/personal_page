# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151023_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
