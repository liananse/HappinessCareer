#!/usr/bin/env python 2.7
# -*- coding: utf-8 -*-

import json
import time
from datetime import datetime
from django.http import HttpResponse

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return int(time.mktime(o.timetuple()))
        return json.JSONEncoder.default(self, 0)


def response_json(result, data, **kw):
    response_result = dict()
    response_result['result'] = result
    response_result['data'] = data

    for k, v in kw.iteritems():
        response_result['%s' % k] = v

    response_json_str = HttpResponse(json.dumps(response_result, DateTimeEncoder), content_type='application/json;charset=utf-8')
    return response_json_str;

def response_json_error(data, **kw):
    return response_json(0, data, **kw)

def response_json_ok(data, **kw):
    return response_json(1, data, **kw)
