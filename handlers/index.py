from handlers.base import BaseHandler

import logging
import tornado.web

logger = logging.getLogger(__name__)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        logger.info('index entry!')
        self.render("index.html")
