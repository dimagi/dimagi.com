from django.conf.urls import url

from dimagi.sectors.views import (
    view_single,
)

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='sector'),
]
