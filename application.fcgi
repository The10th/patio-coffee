#!/home/omegate1/djangoenv/bin/python

# Set up the virtual environment:
import os, sys
os.environ.setdefault('PATH', '/bin:/usr/bin')
os.environ['PATH'] = '/home/omegate1/djangoenv/bin:' + os.environ['PATH']
os.environ['VIRTUAL_ENV'] = '/home/omegate1/djangoenv/bin'
os.environ['PYTHON_EGG_CACHE'] = '/home/omegate1/djangoenv/bin'
os.chdir('/home/omegate1/public_html/patiocoffeeshop.com/pcs')

# Add a custom Python path.
sys.path.insert(0, "/home/omegate1/public_html/patiocoffeeshop.com/pcs")

# Set the DJANGO_SETTINGS_MODULE environment variable to the file in the
# application directory with the db settings etc.
os.environ['DJANGO_SETTINGS_MODULE'] = "pcs.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")