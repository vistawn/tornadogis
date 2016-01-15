# -*- coding:utf-8 -*-
import settings
import glob,os
import json

serviceDict=dict()


def startServer():
    getServices()
    print "services started..."


def reloadServices():
    serviceDict=dict()
    getServices()

    print "services reloaded..."


def getServices():
    service_files = glob.glob(settings.SERVICE_PATH +'/*.ms')
    for f in service_files:
        servicename = os.path.split(f)[1][:-3]
        jfile = open(f)
        serviceDict[servicename] = json.load(jfile)
        jfile.close()

