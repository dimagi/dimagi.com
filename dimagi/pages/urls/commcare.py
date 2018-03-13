from django.conf.urls import url

from dimagi.pages.views.commcare import product, pricing


urlpatterns = [
    url(r'^$', product,
        name='commcare'),
    url(r'^pricing/$', pricing,
        name='commcare_pricing'),
]
