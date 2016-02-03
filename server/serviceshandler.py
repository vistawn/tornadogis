# -*- coding:utf-8 -*-

import os,glob
import json
import math

import server
import settings
import tornado
import db.dbop
import util.tools


class MainHandler(tornado.web.RequestHandler):
    def get(self,*args):
        self.render("welcome.html")


class ServicesListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("services.html",serviceDict = server.services)

class ExportMapHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("export map")

class ServiceInfoHandler(tornado.web.RequestHandler):
    def get(self,path):
        self.set_header("Access-Control-Allow-Origin", "*")
        paths = path.split('/')
        path_len = len(paths)
        if path_len == 1:
            self.get_serviceInfo(paths[0])
        elif path_len == 2:
            if paths[1] == '':
                self.get_serviceInfo(paths[0])
            else:
                self.get_layerInfo(paths[0],paths[1])
        elif path_len == 3:
            if paths[2] == 'query':
                self.query_layer(paths[0],paths[1])
            else:
                self.write("Error 404")
        else:
            self.write("Error 404")


    def get_serviceInfo(self,service_name):
        exp = self.get_argument("export",[])
        if exp <> []:
            self.get_featureMap(service_name)
        else:
            service_json = server.services[service_name].servicejson
            print service_json
            self.render("service_info.html",service = service_json)


    def get_layerInfo(self,service_name,layerid):
        service_json = server.services[service_name].servicejson
        layer = service_json["layers"][int(layerid)]
        print layer
        self.render("layer_info.html",layer=layer)

    def query_layer(self,service_name,layerid):
        service_json = server.services[service_name].servicejson
        layer = service_json["layers"][int(layerid)]
        bbox = self.get_argument("bbox")
        self.write(db.dbop.fetch_json_with_bbox(service_json,int(layerid),layer["layername"],bbox,3))

    def get_featureMap(self,service_name):
        bbox = self.get_argument('bbox')
        pixel_width = self.get_argument('width')
        geo_width = float(bbox.split(',')[2]) - float(bbox.split(',')[0])
        (resolution,scale) = self.calculate_resolution_and_scale(geo_width,float(pixel_width))

        precision = self.get_argument('precision',None,True);

        print resolution,scale

        digi_length = 0
        if precision is None:
            precision = resolution

        digi_length = util.tools.get_float_decimal_length(float(precision))
                    
        print digi_length
        service = server.services[service_name]
        index=0
        output = []
        for layername in service.layers:
            layer = service.layers[layername]
            print layername
            visible = False
            if layer.min_scale > 0 and layer.max_scale > 0:
                if scale < layer.min_scale and scale > layer.max_scale:
                    visible = True

            if layer.min_scale > 0 and layer.max_scale ==0:
                if scale <layer.min_scale:
                    visible = True
            if layer.max_scale > 0 and layer.min_scale ==0:
                if scale > layer.max_scale:
                    visible = True
            if layer.min_scale == 0 and layer.max_scale == 0:
                visible = True

            if visible:
                j = db.dbop.fetch_json_with_bbox(service.service_name,layer.workspace,layer.tablename,bbox,digi_length)
                j["render"] = layer.render
                output.append(j)
        print "======end request======="
        self.write(json.dumps(output))

    def calculate_resolution_and_scale(self,geo_width,pixel_width):
        resolution = geo_width / pixel_width;
        scale = resolution * ((111.32 * 1000)/ 0.0002645833)
        return (resolution,scale)



