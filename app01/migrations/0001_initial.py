# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
                ('pv', models.IntegerField(default=1)),
                ('create_time', models.DateTimeField(default=datetime.datetime(2015, 12, 31, 9, 8, 22, 81145, tzinfo=utc))),
                ('update_time', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
