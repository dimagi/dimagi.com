from django.conf.urls import url

from dimagi.pages.views.open_source import (
    open_source_home,
    open_source_hosting
)


urlpatterns = [
    url(r'^$', open_source_home,
        name='open-source'),
    url(r'^hosting/$', open_source_hosting,
        name='open-source-hosting')
]
