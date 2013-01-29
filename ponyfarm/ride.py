# -*- coding: UTF-8 -*-
import sys
import site
from os.path import dirname, abspath, join

curdir = dirname(abspath(__file__))
sys.path.append(dirname(curdir))
sys.path.append(dirname(dirname(curdir)))
site.addsitedir('/usr/lib/python2.7/dist-packages')

import gtk
import settings
from webkitpony.pony import WebkitPony
    
if __name__ == "__main__":
    client = WebkitPony(settings)
    gtk.main()
    


