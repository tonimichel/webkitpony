import os
from jinja2 import Environment, PackageLoader
from urls import urlconf

PROJECT_DIR = os.getcwd()

# if true context menu and inspector module are enabled
DEBUG = True


# the location of your css
STATIC_URL = '%s/static' % PROJECT_DIR

# the location of upload files
MEDIA_DIR = PROJECT_DIR + '/_data'

# template environment for jinja
TEMPLATE_ENV =  Environment(loader=PackageLoader(PROJECT_DIR.split('/')[-1], 'templates'))

WIDTH = 1200

HEIGHT = 800



URLCONF = urlconf


