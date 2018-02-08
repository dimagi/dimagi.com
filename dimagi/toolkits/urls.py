from django.conf.urls import url

from dimagi.toolkits.views import view_all, view_single, download

urlpatterns = [
    url(r'^$', view_all,
        name='toolkits'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='toolkit_view'),
    url(r'^(?P<slug>[\w-]+)/download/$', download,
        name='toolkit_download'),
]
