from __future__ import absolute_import
from django.conf.urls import url, include
import dimagi.pages.views as pages
from dimagi.case_studies.views import view_all as case_studies


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
    url(r'^case-studies/$', case_studies,
        name='case_studies'),
    url(r'^case-study/',
        include('dimagi.case_studies.urls')),
    url(r'^toolkits/',
        include('dimagi.toolkits.urls')),
    url(r'^blog/',
        include('dimagi.blog.urls')),
    url(r'^sectors/',
        include('dimagi.sectors.urls')),
    url(r'^about/$', pages.about,
        name='about'),
    url(r'^careers/$', pages.careers,
        name='careers'),
    url(r'^contact/$', pages.contact,
        name='contact'),
]
