# -*- coding:utf-8 -*-
import settings
import glob,os
import json
import db.dbop
import service

serviceDict={}


def startServer():
    getServices()
    print "services started..."


def reloadServices():
    serviceDict={}
    getServices()

    print "services reloaded..."


def getServices():
    service_files = glob.glob(settings.SERVICE_PATH +'/*.ms')
    for f in service_files:
        servicename = os.path.split(f)[1][:-3]
        jfile = open(f)
        service_json = json.load(jfile)
        serviceWorkspaces = openWorkspace(servicename,service_json)
        serviceDict[servicename] = service_json
        jfile.close()

def openWorkspace(servicename,service_json):
    workspaceconfig = service_json["workspace"]
    for x in workspaceconfig:
        db.dbop.connectdb(servicename,x,workspaceconfig[x])

