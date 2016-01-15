# -*- coding:utf-8 -*-
import tornado
from services import serviceshandler

handlers = [
    (r"/",serviceshandler.MainHandler),
    (r"/services",serviceshandler.ServicesListHandler),
    (r"/services/",serviceshandler.ServicesListHandler),
    (r"/services/(.*)",serviceshandler.ServiceInfoHandler)
]