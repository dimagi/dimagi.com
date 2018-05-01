from django.conf.urls import url

from dimagi.pages.views.terms import (
    default,
    get_terms,
)

urlpatterns = [
    url(r'^$', default, name='terms_default'),
    url(r'^(?P<version>[\w-]+)/$', get_terms, name='terms_version'),
    url(r'^(?P<version>[\w-]+)/(?P<slug>[\w-]+)/$', get_terms, name='terms'),
]
