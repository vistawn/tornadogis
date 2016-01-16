# -*- coding:utf-8 -*-
import tornado
from server import serviceshandler

handlers = [
    (r"/",serviceshandler.MainHandler),
    (r"/services",serviceshandler.ServicesListHandler),
    (r"/services/",serviceshandler.ServicesListHandler),
    (r"/services/(.*)",serviceshandler.ServiceInfoHandler)
]