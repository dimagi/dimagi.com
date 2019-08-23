from django.conf.urls import url

from dimagi.pages.views.focus_mdm import (
    product_mdm,
    pricing_mdm
)


urlpatterns = [
    url(r'^$', product_mdm,
        name='focus_mdm'),
    url(r'^pricing/$', pricing_mdm,
        name='focus_mdm_pricing')
]
