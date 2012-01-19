import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

# Django settings for mw_cms project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_TOOLBAR_ACTIVE = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'mw_db.sqlite3'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'it'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collectstatic')
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'#'/media/admin/'

ADMIN_URL_PREFIX = '/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)
#INTERNAL_IPS = ('127.0.0.1',)# DEBUG

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'mw_cms.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    
    'south',
    'mptt',
    'filebrowser',
    'feincms',
    
    'treepages',
        'tinymce',

    'google_analytics', 

)

#if DEBUG_TOOLBAR_ACTIVE:
    #try:
        #import debug_toolbar_settings
       
        #MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + getattr(debug_toolbar_settings, "DEBUG_TOOLBAR_MIDDLEWARE_CLASSES", ())
        #INSTALLED_APPS = INSTALLED_APPS + getattr(debug_toolbar_settings, "DEBUG_TOOLBAR_INSTALLED_APPS", ())
        
        #INTERNAL_IPS = getattr(debug_toolbar_settings, "DEBUG_TOOLBAR_INTERNAL_IPS", ())
        #DEBUG_TOOLBAR_CONFIG = getattr(debug_toolbar_settings, "DEBUG_TOOLBAR_DEBUG_TOOLBAR_CONFIG", ())
        
    #except ImportError:
        #pass
#try:
    #from database_settings import *
#except ImportError:
    #print "database_settings module not found. Default settings are used."
#try:
    #from local_settings import *
#except ImportError:
    #print "local_settings module not found. Default settings are used."

LANGUAGES = (
    ('it', 'Italiano'),
    )

# google analytics
GOOGLE_ANALYTICS_MODEL = True

# tinymce
TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = STATIC_ROOT + 'tiny_mce/'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table, paste, searchreplace, advlink, advimage, inlinepopups, media, fullscreen",
    'theme_advanced_buttons1' : "undo, redo, separator, paste, pasteword, separator, bold, italic, underline, strikethrough, separator, justifyleft, justifycenter, justifyright, justifyfull, separator, outdent, indent, separator, formatselect, fontsizeselect, removeformat",
    'theme_advanced_buttons2' : "bullist, numlist, separator, image, link, unlink, media, hr, charmap, anchor, table, separator, visualaid, tablecontrols",
    'theme_advanced_buttons3' : "fullscreen, separator, search, replace, separator, cleanup, code",
    'dialog_type' : "modal",
    'theme': "advanced",
    'theme_advanced_toolbar_location' : "top",
    'skin' : "o2k7",
    'relative_urls' : False,
    'language': "it",
    'height' : "500",
    'width' : "80%",
}
TINYMCE_FILEBROWSER = True
#filebrowser
FILEBROWSER_DIRECTORY = os.path.join(MEDIA_ROOT, 'filebrowser_uploads')
FILEBROWSER_SAVE_FULL_URL = True
FILEBROWSER_DEBUG = DEBUG

FEINCMS_PAGE_USE_CHANGE_LIST = True
#FEINCMS_ADMIN_MEDIA = '/media/feincms/' #os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/feincms/')
FEINCMS_ADMIN_MEDIA_HOTLINKING = False

#import django
#if django.VERSION[0]==1 and django.VERSION[1]>=3:
    ## can use django.contrib.staticfiles
    #pass

