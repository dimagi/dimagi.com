from __future__ import absolute_import
from django.conf.urls import url, include
import dimagi.pages.views as pages


urlpatterns = [
    url(r'^$', pages.home,
        name='home'),
    url(r'^services/$', pages.services,
        name='services'),
    url(r'^contact/$', pages.contact,
        name='contact'),
    url(r'^commcare/',
        include('dimagi.pages.urls.commcare')),
    url(r'^case-studies/',
        include('dimagi.pages.urls.case_studies')),
    url(r'^toolkits/',
        include('dimagi.pages.urls.toolkits')),
    url(r'^blog/',
        include('dimagi.pages.urls.blog')),
    url(r'^sectors/',
        include('dimagi.pages.urls.sectors')),
    url(r'^about/',
        include('dimagi.pages.urls.about')),
    url(r'^careers/',
        include('dimagi.pages.urls.careers')),
    url(r'^press/',
        include('dimagi.pages.urls.press')),
    url(r'^policy/',
        include('dimagi.pages.urls.policies')),
]
