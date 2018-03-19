from django.conf.urls import url

from dimagi.pages.views.commcare import product, pricing, product_test


urlpatterns = [
    url(r'^$', product,
        name='commcare'),
    url(r'^test/$', product_test,
        name='commcare_test'),
    url(r'^pricing/$', pricing,
        name='commcare_pricing'),
]
