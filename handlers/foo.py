from handlers.base import BaseHandler

import logging
import tornado.web

logger = logging.getLogger(__name__)


class FooHandler(tornado.web.RequestHandler):
    def get(self):
        logger.info('foo entry!')
        self.render("index.html")
