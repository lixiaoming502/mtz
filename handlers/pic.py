from handlers.base import BaseHandler

import logging
import tornado.web

class PicHandles(tornado.web.RequestHandler):

    BASE_PIC_DIR = '/Users/lixiaoming/Documents/meizitu/所有/'

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        data={}
        data['pic_id']=self.request.uri.split('/')[-1:][0]
        if data['pic_id']:
          yield self.myopen(data['pic_id'])
        else:
            self.write("no url")
    
    def myopen(self,pic_id):
         with open('/Users/lixiaoming/Documents/meizitu/所有/'+pic_id,'rb') as pic:
            pics = pic.read()
            # result=base64.encodestring(pics)
            self.write(pics)
            self.set_header("Content-type", "image/png")