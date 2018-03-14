from django.conf.urls import url

from dimagi.pages.views.press import view_all


urlpatterns = [
    url(r'^$', view_all, name='press'),
    url(r'^(?P<page>[\d]+)/$', view_all, name='press_page'),
]
