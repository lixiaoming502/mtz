import os
import tornado
import tornado.template
from tornado.options import define,options


path = lambda  root,*a:os.path.join(root,*a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port",default=8000,help="run on the given port",type=int)
define("config",default=None,help="tornado config file")
define("debug",default=False,help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = path(ROOT,'media')
TEMPLATE_ROOT = path(ROOT,'templates')

class DeploymentType:
    PRODUCTION = "PRODUCION"
    DEV = "DEV"
    SOLO = "SOLO"
    STAGING = "STAGING"
    dict = {
        SOLO:1,
        PRODUCTION:2,
        DEV:3,
        STAGING:4
    }
if 'DEPLOYMENT_TYPE' in os.environ:
    DEPLOYMENT = os.environ['DEPLOYMENT_TYPE'].upper()
else:
    DEPLOYMENT = DeploymentType.SOLO

settings = {}
settings['debug'] = DEPLOYMENT!=DeploymentType.PRODUCTION or options.debug
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = "yD4HIcu3Hv91/PR8"
settings['xsrf_cookies'] = True
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)



