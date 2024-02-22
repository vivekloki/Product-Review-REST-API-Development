import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = True
    PORT = 5000
 

configs = dict(
    dev=Config,
)

Config_is = configs[os.environ.get('CONFIG', 'dev')]
