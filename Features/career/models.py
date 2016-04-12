#!/usr/bin/env python 2.7
# -*- coding: utf-8 -*-

from django.db import models

class Career(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'职业名称')
    description = models.TextField(verbose_name=u'职业简介')
    create_date = models.DateField(auto_now_add=True, verbose_name=u'创建日期')

    class Meta:
        verbose_name = u'职业管理'
        verbose_name_plural = u'职业管理'