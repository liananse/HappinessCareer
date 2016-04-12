# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u804c\u4e1a\u540d\u79f0')),
                ('description', models.TextField(verbose_name='\u804c\u4e1a\u7b80\u4ecb')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
            ],
            options={
                'verbose_name': '\u804c\u4e1a\u7ba1\u7406',
                'verbose_name_plural': '\u804c\u4e1a\u7ba1\u7406',
            },
        ),
    ]
