import yaml
import os
import platform

if platform.system() == 'Windows':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
else:
    BASE_DIR = '/data/conf/cmdb-server'

try:
    with open(BASE_DIR + os.path.sep + 'settings.yml', 'rb') as ymlfile:
        settings = yaml.load(ymlfile)
except:
    pass
