#!/usr/bin/env python 2.7
# -*- coding: utf-8 -*-

from models import Career
from django.views.decorators.csrf import csrf_exempt
from libs.restful_utils import response_json_error, response_json_ok

@csrf_exempt
def addCareer(request):
    career_name = request.POST.get('careerName', '')
    career_des = request.POST.get('careerDes', '')

    if career_name is None or len(career_name) <= 0:
        return response_json_error('', msg='career name is empty')

    if career_des is None or len(career_des) <= 0:
        return response_json_error('', msg='career description is empty')

    career = Career()
    career.name = career_name
    career.description = career_des

    career.save()

    return response_json_ok('')