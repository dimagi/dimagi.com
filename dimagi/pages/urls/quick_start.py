from django.conf.urls import url

from dimagi.pages.views.quick_start import view_all, view_single


urlpatterns = [
    url(r'^$', view_all,
        name='quick_start'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='quick_start_area'),
]
