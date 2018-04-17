import tornado.httpserver
import tornado.ioloop
import logging
from settings import settings
from urls import url_patterns
from tornado.options import options

logger = logging.getLogger(__name__)

class MyApp(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,url_patterns,**settings)

def main():
    logger.info('start begin!')
    app = MyApp()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    logger.info('io begin! listen at %s' % options.port)
    tornado.ioloop.IOLoop.instance().start()
    logger.info('start done!!')


if __name__=="__main__":
    main()