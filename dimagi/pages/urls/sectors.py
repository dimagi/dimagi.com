from django.conf.urls import url

from dimagi.pages.views.sectors import (
    view_all,
    view_single,
    sector_reproductive_health,
)


urlpatterns = [
    url(r'^$', view_all,
        name='sectors'),
    url(r'^reproductive-health/$', sector_reproductive_health,
        name='sector_reproductive_health'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='sector'),
]
