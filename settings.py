# -*- coding:utf-8 -*-

import os

# server running port
SERVER_PORT = 8888

# server template folder
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates')

# static files folder
STATIC_PATH = os.path.join(os.path.dirname(__file__), 'static')

#
XSRF_COOKIES = True


COOKIE_SECRET = 'xNF3PmAtTRqXel5eOAmsj3ohhC7bj0VclTkkRLHJ1VE='

DEBUG = True


CONFIG_PATH=os.path.join(os.path.dirname(__file__), 'config')

## gis services file path
SERVICE_PATH=os.path.join(CONFIG_PATH, 'services')

LOG_PATH=os.path.join(os.path.dirname(__file__), 'log')

### log level
#  4 DEBUG   print everything
#  3 DETAIL  print exception and request and response
#  2 ERROR   print exception
#  1 BASE   always log 
LOG_LEVEL = 4