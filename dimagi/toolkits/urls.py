from django.conf.urls import url

from dimagi.toolkits.views import view_all, view_single

urlpatterns = [
    url(r'^$', view_all,
        name='toolkits'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='toolkit'),
]
