from handlers.foo import FooHandler
from handlers.index import IndexHandler
from handlers.pic import PicHandles

url_patterns = [
    (r"/foo", FooHandler),
    (r"/", IndexHandler),
    (r"/pic/*.*",PicHandles),
]
