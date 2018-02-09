from django.conf.urls import url

from dimagi.sectors.views import (
    view_all,
    view_single,
)

urlpatterns = [
    url(r'^$', view_all,
        name='sectors'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='sector'),
]
