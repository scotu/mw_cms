======
README
======

mw_cms is a demonstration project (a content management system) for the `django-treepages`_ app written using the `Django web framework`_.

.. _`django-treepages`: https://github.com/scotu/django-treepages
.. _`Django web framework`: http://djangoproject.com

Requires django 1.3 at the moment because it is using contrib.staticfiles

----------
Try it out
----------

If you are not using virtualenv (and virtualenvwrapper), you should. 

Create and activate a virtualenv::

    sudo apt-get install build-essential python-dev # needed to compile PIL, command for ubuntu, adjust for your distro
    mkvirtualenv --no-site-packages cms
    cdvirtualenv
    mkdir git && cd git

Than clone this repository and install dependencies::

    git clone https://github.com/scotu/mw_cms
    pip install -r mw_cms/requirements.txt
    pip install -r ../src/django-treepages/requirements.txt
    cd mw_cms/mw_cms/
    ./manage.py runserver

The username and password in the included sqlite database are both 'admin'.
At the moment it lacks an homepage, just open http://localhost:8000/admin/
