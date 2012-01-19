import os, sys

# activate virtualenv
activate_this = os.path.expanduser("/home/USER/.virtualenvs/VIRTUALENVNAME/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# tell django where our settings module is
sys.path.insert(0, os.path.expanduser(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'mw_cms.settings'

# run django
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
