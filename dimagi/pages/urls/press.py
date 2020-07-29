from django.conf.urls import url

from dimagi.pages.views.press import in_news


urlpatterns = [
    url(r'^$', in_news, name='press'),
]
