# -*- coding:utf-8 -*-

import os,sys,datetime
import tornado.ioloop
import tornado.web
import urls
import settings as setting_const
import server.server


reload(sys)
sys.setdefaultencoding('utf-8')

for arg in sys.argv:
    if arg.startswith('--'):
        param = arg[2:].split('=')[0]
        value = arg[2:].split('=')[1]
        if param.lower() == 'debug':
            print param,value
        elif param.lower() == 'log':
            print param,value

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

        server.server.start_server()


if __name__ == "__main__":
    application = Application()
    application.listen(setting_const.SERVER_PORT)
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