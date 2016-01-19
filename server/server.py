# -*- coding:utf-8 -*-
import settings
import glob,os
import json
import db.dbop
from service import Service
from service import Layer

services = {}


def start_server():
    get_services()
    print "services started..."


def reload_services():
    get_services()

    print "services reloaded..."


def get_services():
    service_files = glob.glob(settings.SERVICE_PATH +'/*.ms')
    for f in service_files:
        servicename = os.path.split(f)[1][:-3]
        jfile = open(f)
        service_json = json.load(jfile)
        services[servicename] = get_service_object(service_json)
        serviceWorkspaces = open_workspace(servicename,service_json)
        jfile.close()

def open_workspace(servicename,service_json):
    workspaceconfig = service_json["workspace"]
    for x in workspaceconfig:
        db.dbop.connectdb(servicename,x,workspaceconfig[x])

def get_service_object(service_json):
    servicename = service_json["name"]
    service = Service(servicename,service_json)
    layers_json = service_json["layers"]
    for layer_json in layers_json:
        layername = layer_json["layername"]
        print "add layer :" + layername
        layer = Layer(layername)
        layer.workspace = layer_json["datasource"]["workspace"]
        layer.tablename = layer_json["datasource"]["dataname"]
        layer.min_scale = layer_json["min_scale"]
        layer.max_scale = layer_json["max_scale"]
        layer.render = layer_json["renderer"]
        service.layers[layername] = layer
    return service
