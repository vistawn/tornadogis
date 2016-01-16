# -*- coding:utf-8 -*-

import os,glob
import json
import server
import layer
import settings
import tornado
import db.dbop

class MainHandler(tornado.web.RequestHandler):
    def get(self,*args):
        self.render("welcome.html")


class ServicesListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("services.html",serviceDict = services.serviceDict)

class ExportMapHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("export map")

class ServiceInfoHandler(tornado.web.RequestHandler):
    def get(self,path):
        self.set_header("Access-Control-Allow-Origin", "*")
        paths = path.split('/')
        path_len = len(paths)
        if path_len == 1:
            self.getServiceInfo(paths[0])
        elif path_len == 2:
            if paths[1] == '':
                self.getServiceInfo(paths[0])
            else:
                self.getLayerInfo(paths[0],paths[1])
        elif path_len == 3:
            if paths[2] == 'query':
                self.queryLayer(paths[0],paths[1])
            else:
                self.write("Error 404")
        else:
            self.write("Error 404")


    def getServiceInfo(self,service_name):
        exp = self.get_argument("export",[])
        if exp <> []:
            self.getFeatureMap(service_name)
        else:
            service_json = server.serviceDict[service_name]
            self.render("service_info.html",service = service_json)


    def getLayerInfo(self,service_name,layerid):
        service_json = server.serviceDict[service_name]
        layer = service_json["layers"][int(layerid)]
        self.render("layer_info.html",layer=layer)

    def queryLayer(self,service_name,layerid):
        service_json = server.serviceDict[service_name]
        layer = service_json["layers"][int(layerid)]
        bbox = self.get_argument("bbox")
        self.write(db.dbop.fetch_json_with_bbox(service_json,int(layerid),layer["layername"],bbox))

    def getFeatureMap(self,service_name):
        bbox = self.get_argument('bbox')
        service_json = server.serviceDict[service_name]
        index=0
        output = []
        for x in service_json["layers"]:
            j = db.dbop.fetch_json_with_bbox(service_json,index,x["layername"],bbox)
            if x["layername"] == "prefecture_polygon":
                j["style"] = {"weight": 2,
                "color": "#999",
                "opacity": 1,
                "fillColor": "#B0DE5C",
                "fillOpacity": 0.8}
            output.append(j)
        #print output
        self.write(json.dumps(output))



