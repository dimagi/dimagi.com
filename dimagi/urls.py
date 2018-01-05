from __future__ import absolute_import
from django.conf.urls import url
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
    url(r'^case_studies/$', pages.case_studies,
        name='case_studies'),
    url(r'^toolkits/$', pages.toolkits,
        name='toolkits'),
    url(r'^blog/$', pages.blog,
        name='blog'),
    url(r'^about/$', pages.about,
        name='about'),
    url(r'^careers/$', pages.careers,
        name='careers'),
]
