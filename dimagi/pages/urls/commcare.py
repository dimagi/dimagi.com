from django.conf.urls import url

from dimagi.pages.views.commcare import (
    product,
    product_features,
    research,
    commcare_onboarding,
    commcare_integration,
    pricing,
    handle_pricing_pdf,
)


urlpatterns = [
    url(r'^$', product,
        name='commcare'),
    url(r'^features/$', product_features,
        name='commcare_features'),
    url(r'^research/$', research,
        name='research'),
    url(r'^onboarding/$', commcare_onboarding,
        name='commcare_onboarding'),
    url(r'^integrations/$', commcare_integration,
        name='commcare_integration'),
    url(r'^pricing/$', pricing,
        name='commcare_pricing'),
    url(r'^pricing/commcare-pricing-monthly.pdf$', handle_pricing_pdf(True),
        name='monthly_commcare_pricing_pdf'),
    url(r'^pricing/commcare-pricing-annual.pdf$', handle_pricing_pdf(False),
        name='annual_commcare_pricing_pdf'),
]
