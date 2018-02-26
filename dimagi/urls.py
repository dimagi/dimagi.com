from __future__ import absolute_import
from django.conf.urls import url, include
import dimagi.pages.views as pages


urlpatterns = [
    url(r'^$', pages.home,
        name='home'),
    url(r'^products/commcare/$', pages.products_commcare,
        name='products_commcare'),
    url(r'^products/commcare/pricing/$', pages.pricing_commcare,
        name='pricing_commcare'),
    url(r'^services/$', pages.services,
        name='services'),
    url(r'^services/pricing/$', pages.pricing_services,
        name='pricing_services'),
    url(r'^case-studies/',
        include('dimagi.case_studies.urls')),
    url(r'^toolkits/',
        include('dimagi.toolkits.urls')),
    url(r'^blog/',
        include('dimagi.blog.urls')),
    url(r'^sectors/',
        include('dimagi.sectors.urls')),
    url(r'^about/',
        include('dimagi.about.urls')),
    url(r'^careers/',
        include('dimagi.careers.urls')),
    url(r'^contact/$', pages.contact,
        name='contact'),
]
