from __future__ import absolute_import
from django.conf.urls import url
import dimagi.pages.views as pages


urlpatterns = [
    url(r'^$', pages.home, name='page_home'),
    url(r'^products/$', pages.products, name='page_products'),
]
