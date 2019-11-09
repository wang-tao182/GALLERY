# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, default='文章标题')),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='images/', default='default.png')),
                ('text', models.TextField(default='正文')),
            ],
        ),
    ]
