from django.conf.urls import patterns, include, url
from django.contrib import admin

from fortytwo_test_task import settings

admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'apps.contact.views.home_page', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# If this is in DEBUG/runserver mode, did you remember to add to your urls.py
if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^uploads/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT,
                                 }),
                            url(r'^static/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.STATIC_ROOT,
                                 }),
                            )
