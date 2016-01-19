# -*- coding:utf-8 -*-
import collections

class Service(object):
    service_name = ''
    servicejson = {}
    layers = collections.OrderedDict()
    def __init__(self,in_service_name,in_service_json):
        self.service_name = in_service_name
        self.servicejson = in_service_json


class Layer(object):
    layer_name = ''
    workspace = ''
    tablename = ''
    min_scale = 0
    max_scale = 0
    render = None  
    cursor = None
    def __init__(self,layername):
        layer_name = layername

