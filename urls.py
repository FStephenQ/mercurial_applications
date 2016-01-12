from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#from . import views
from mercurial_applications.core_page import views
from mercurial_applications.blog import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core_page.views.index'),
    # url(r'^mercurial_applications/', include('mercurial_applications.foo.urls')),
    url(r'^blog/','blog.views.front'),
    url(r'^bio/','core_page.views.bio'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
