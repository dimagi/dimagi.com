from __future__ import absolute_import
from django.shortcuts import render
from dimagi.utils.decorators import no_index
from dimagi.utils.partners import get_logos


@no_index
def product(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/commcare/product.html', context)


@no_index
def pricing(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/commcare/pricing.html', context)
