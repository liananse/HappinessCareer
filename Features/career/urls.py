#!/usr/bin/env python 2.7
# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^api/career/addCareer', addCareer)
]