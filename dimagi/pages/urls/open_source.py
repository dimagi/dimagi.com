from django.conf.urls import url

from dimagi.pages.views.open_source import (
    open_source_home
)


urlpatterns = [
    url(r'^$', open_source_home,
        name='open-source'),
]
