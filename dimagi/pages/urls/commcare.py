from django.conf.urls import url

from dimagi.pages.views.commcare import product, pricing, partners


urlpatterns = [
    url(r'^$', product,
        name='commcare'),
    url(r'^pricing/$', pricing,
        name='commcare_pricing'),
    url(r'^partners/$', partners,
        name='partner_program'),
]
