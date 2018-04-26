from __future__ import absolute_import
from django.shortcuts import render

from dimagi.utils.partners import get_logos
from dimagi.data.commcare.pricing import feature_groups


def _get_global_context():
    return {
        'partners': get_logos(),
    }


def product(request):
    context = _get_global_context()
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - CommCare (top fold)"
    return render(request, 'pages/commcare/product.html', context)


def pricing(request):
    context = _get_global_context()
    context['feature_groups'] = [g.GROUP for g in feature_groups]
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - Pricing Top"
    return render(request, 'pages/commcare/pricing.html', context)


def partners(request):
    return render(request, 'pages/commcare/partners.html')
