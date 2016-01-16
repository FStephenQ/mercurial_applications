from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

#from . import views
from core_page import views as core_views
from blog import views as blog_views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', core_views.index),
    # url(r'^mercurial_applications/', include('mercurial_applications.foo.urls')),
    url(r'^blog/tag/([?P<tagname>[a-z]+)/$',blog_views.tag),
    url(r'^blog/$',blog_views.front),
    url(r'^bio/',core_views.bio),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
