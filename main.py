# -*- coding:utf-8 -*-

import os,sys,datetime
import tornado.ioloop
import tornado.web
from db import dbop
import urls
import settings as setting_const
import services.services


reload(sys)
sys.setdefaultencoding('utf-8')

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls.handlers
        print 'reloaded ' + datetime.datetime.now().isoformat() 
        settings = dict(
        # template folder
        template_path = setting_const.TEMPLATE_PATH,
        
        # static files folder
        static_path = setting_const.STATIC_PATH,

        gzip=True,

        # 防止跨站伪造请求
        xsrf_cookies = setting_const.XSRF_COOKIES,

        cookie_secret=setting_const.COOKIE_SECRET,

        debug=setting_const.DEBUG
        )

        tornado.web.Application.__init__(self,handlers,**settings)

        services.services.startServer()


if __name__ == "__main__":
    application = Application()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()





class LayersHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        

        bbox = self.get_argument("bbox")
        self.write(dbop.fetch_json_with_bbox(layername,bbox))

# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#         (r"/query",LayersHandler)
#     ])

# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()