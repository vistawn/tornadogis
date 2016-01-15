# -*- coding:utf-8 -*-

import os

SERVER_PORT = 8888
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")
XSRF_COOKIES = True
COOKIE_SECRET = "11oJp2ksdFuYhuAddEVoP1o/XKTze7eQnEL5gTJujH7="
DEBUG = True
CONFIG_PATH=os.path.join(os.path.dirname(__file__), "config")
SERVICE_PATH=os.path.join(CONFIG_PATH, "services")