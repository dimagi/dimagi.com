from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import render

from dimagi.utils.ab_tests import DEMO_WORKFLOW
from dimagi.utils.decorators.enable_ab_test import enable_ab_test
from dimagi.utils.partners import get_logos
from dimagi.data.commcare.pricing import feature_groups
from dimagi.utils.pdf.pricing import get_pricing_pdf


def _get_global_context():
    return {
        'partners': get_logos(),
    }


@enable_ab_test(DEMO_WORKFLOW)
def product(request):
    context = _get_global_context()
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - CommCare (top fold)"
    return render(request, 'pages/commcare/product.html', context)


@enable_ab_test(DEMO_WORKFLOW)
def pricing(request):
    context = _get_global_context()
    context['feature_groups'] = [g.GROUP for g in feature_groups]
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - Pricing Top"
    return render(request, 'pages/commcare/pricing.html', context)


def handle_pricing_pdf(is_monthly):

    def pricing_pdf(request):
        filename = "commcare-pricing-{}.pdf".format(
            "monthly" if is_monthly else "annual"
        )
        data = get_pricing_pdf(
            [g.GROUP for g in feature_groups],
            is_monthly=is_monthly
        )
        response = HttpResponse(data, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
        data.close()
        return response

    return pricing_pdf


def partners(request):
    return render(request, 'pages/commcare/partners.html')
