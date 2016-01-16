# -*- coding:utf-8 -*-

class service(object):
    service_name = ''
    layers = []
    def __init__(self,service_name):
        service_name = service_name

class render(object):
    render_type=''
    styles = {}


class layer(object):
    layer_name = ''
    workspace = ''
    tablename = ''
    render = render()
    def __init__(self,layername,workspacename,tablename):
        layer_name = layername
        workspace = workspacename
        tablename = tablename

    def set_style(self,fieldname,style):
        render.styles[fieldname] = style