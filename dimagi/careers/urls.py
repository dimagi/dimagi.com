from django.conf.urls import url

from dimagi.careers.views import home


urlpatterns = [
    url(r'^$', home,
        name='careers'),
]
