"""temp URL Configuration
"""
# import django
from django.conf import settings
from django.conf.urls import url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^$', "users.views.home" ),
    url(r'^admin/', admin.site.urls),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',  'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, } ),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, } ),
    )
