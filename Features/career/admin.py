#!/usr/bin/env python 2.7
# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Career

class CareerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)

admin.site.register(Career, CareerAdmin)