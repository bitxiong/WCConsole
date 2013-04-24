from django.conf.urls import patterns, include, url
from WCT.date import current_datetime
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from wcAP1.search import search
from wcAP1.views import contact,index,wcrequest,wcHook,test
from wcAP1.wchooker import wcInfoHandler
from wcAP1.webCrawler import testCrawler
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WCT.views.home', name='home'),
    # url(r'^WCT/', include('WCT.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^wcreq',wcHook),
    url(r'^admin/', include(admin.site.urls)),
	#(r'^admin/', include('wcAP1.admin.site.urls')),
	(r'^now/$',current_datetime),
	(r'^search/$', search),
	(r'^contact/$', contact),
    (r'^test/',test),
    (r'^crawl/',testCrawler),
    (r'^gossip/',wcHook)
)