from django.conf.urls import url

from dimagi.pages.views.commcare import (
    product,
    product_features,
    research,
    commcare_onboarding,
    commcare_integration,
    commcare_messaging,
    pricing,
    handle_pricing_pdf,
    monitoring_evaluation,
    ict4d,
    vaccine_delivery,
    enterprise,
    classroom
)


urlpatterns = [
    url(r'^$', product,
        name='commcare'),
    url(r'^monitoring-evaluation/$', monitoring_evaluation,
        name='monitoring_evaluation'),
    url(r'^ict4d/$', ict4d,
        name='ict4d'),
    url(r'^features/$', product_features,
        name='commcare_features'),
    url(r'^research/$', research,
        name='research'),
    url(r'^onboarding/$', commcare_onboarding,
        name='commcare_onboarding'),
    url(r'^integrations/$', commcare_integration,
        name='commcare_integration'),
    url(r'^messaging/$', commcare_messaging,
        name='commcare_messaging'),
    url(r'^pricing/$', pricing,
        name='commcare_pricing'),
    url(r'^enterprise/$', enterprise,
        name='enterprise'),
    url(r'^vaccine-delivery/$', vaccine_delivery,
        name='vaccine_delivery'),
    url(r'^pricing/commcare-pricing-monthly.pdf$', handle_pricing_pdf(True),
        name='monthly_commcare_pricing_pdf'),
    url(r'^pricing/commcare-pricing-annual.pdf$', handle_pricing_pdf(False),
        name='annual_commcare_pricing_pdf'),
    url(r'^classroom/$', classroom,
        name='classroom'),
]
