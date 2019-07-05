from django.conf.urls import url


from dimagi.pages.views.sectors import (
    view_all,
    view_single,
    maternal_and_child_health,
)


urlpatterns = [
    url(r'^$', view_all,
        name='sectors'),
    url(r'^maternal-and-child-health/$', maternal_and_child_health,
        name='maternal_and_child_health'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='sector'),
]
