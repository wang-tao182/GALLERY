# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default='在这里写作品简介', max_length=200)),
                ('FIELDONME', models.ImageField(default='default.png', upload_to='images/')),
                ('title', models.CharField(default='production', max_length=50)),
            ],
        ),
    ]
