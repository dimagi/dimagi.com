from django.conf.urls import url

from dimagi.press.views import view_all

urlpatterns = [
    url(r'^$', view_all, name='press'),
]
