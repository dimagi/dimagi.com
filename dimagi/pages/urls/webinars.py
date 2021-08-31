from django.conf.urls import url

from dimagi.pages.views.webinars import view_all, view_single


urlpatterns = [
    url(r'^$', view_all,
        name='webinars'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='webinar'),
]
