from django.conf.urls import url

from dimagi.pages.views.sectors import (
    view_all,
    view_single,
    disease_treatment
)


urlpatterns = [
    url(r'^$', view_all,
        name='sectors'),
    url(r'^disease-treatment/$', disease_treatment,
        name='disease_treatment'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='sector'),
]
