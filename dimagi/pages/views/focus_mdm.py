from __future__ import absolute_import

from django.shortcuts import render

from dimagi.utils.ab_tests import DEMO_WORKFLOW_V2
from dimagi.utils.decorators.enable_ab_test import enable_ab_test
from dimagi.utils.partners import get_logos
from dimagi.data.commcare.pricing import feature_groups


def _get_global_context():
    return {
        'partners': get_logos(),
    }


@enable_ab_test(DEMO_WORKFLOW_V2)
def product_mdm(request):
    context = _get_global_context()
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - CommCare (top fold)"
    return render(request, 'pages/focus_mdm/product.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def pricing_mdm(request):
    context = _get_global_context()
    context['feature_groups'] = [g.GROUP for g in feature_groups]
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - Pricing Top"
    return render(request, 'pages/focus_mdm/pricing.html', context)
