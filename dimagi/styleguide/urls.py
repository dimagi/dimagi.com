from django.conf.urls import url

from dimagi.styleguide.views import home


urlpatterns = [
    url(r'^$', home, name='styleguide'),
]
