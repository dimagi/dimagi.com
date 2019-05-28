from django.conf.urls import url

from dimagi.pages.views.sectors import (
    view_all,
    view_single,
    nutrition_programs
)


urlpatterns = [
    url(r'^$', view_all,
        name='sectors'),
    url(r'^nutrition/$', nutrition_programs,
        name='agriculture_extension_programs'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='sector'),
]
