from __future__ import absolute_import
from django.shortcuts import render
from dimagi.utils.decorators import no_index
from dimagi.utils.partners import get_logos
from dimagi.data.commcare.pricing import feature_groups


def _get_global_context():
    return {
        'partners': get_logos(),
    }


@no_index
def product(request):
    context = _get_global_context()
    return render(request, 'pages/commcare/product.html', context)


@no_index
def pricing(request):
    context = _get_global_context()
    context['feature_groups'] = [g.GROUP for g in feature_groups]
    return render(request, 'pages/commcare/pricing.html', context)
