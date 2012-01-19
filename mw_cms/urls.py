from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from sitemaps import SitoSitemap

admin.autodiscover()

admin_prefix = settings.ADMIN_URL_PREFIX.strip('/')

sitemaps_dict = {
    'sito': SitoSitemap,
}

urlpatterns = patterns('',
    # Static homepage:
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'homepage.html'}),
    
    # sitemap
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps_dict}),

    # django-email-usernames
    #(r'^accounts/', include('email_usernames.urls')),

    # django-attachments
    (r'^attachments/', include('attachments.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^%s/doc/' % admin_prefix, include('django.contrib.admindocs.urls')),

    # django-tinymce
    (r'^tinymce/', include('tinymce.urls')),
    
    # django-filebrowser
    (r'^%s/filebrowser/' % admin_prefix, include('filebrowser.urls')),
    
    # Uncomment the next line to enable the admin:
    (r'^%s/' % admin_prefix, include(admin.site.urls)),

)
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    import os
    # get the user-uploaded media path from settings
    media_url = settings.MEDIA_URL
    if media_url.startswith('/'):
        media_url = media_url.lstrip('/')
    if media_url.endswith('/'):
        media_url = media_url.rstrip('/')
    urlpatterns += patterns('',
        (
            r'^%s/(?P<path>.*)$' % media_url,
            #r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),

    )
urlpatterns += patterns('',
    url(r'^$|^(.*)/$', 'treepages.views.base_url_page_handler'),
    )
