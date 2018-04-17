from handlers.base import BaseHandler

import logging
import tornado.web

class PicHandles(tornado.web.RequestHandler):
    BASE_PIC_DIR = '/Users/lixiaoming/Documents/meizitu/所有/'
    def get(self):
        data={}
        data['pic_id']=self.request.uri.split('/')[-1:][0]
        if data['pic_id']:
          pic=open('/Users/lixiaoming/Documents/meizitu/所有/test.jpg','rb')
          pics=pic.read()
          # result=base64.encodestring(pics)
          self.write(pics)
          self.set_header("Content-type", "image/png")
        else:
            self.write("no url")