from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import render

from dimagi.utils.ab_tests import DEMO_WORKFLOW_V2
from dimagi.utils.decorators.enable_ab_test import enable_ab_test
from dimagi.utils.partners import get_logos
from dimagi.utils.enterprise_partners import get_enterprise_partners
from dimagi.data.commcare.pricing import feature_groups
from dimagi.utils.pdf.pricing import get_pricing_pdf


def _get_global_context():
    return {
        'partners': get_logos(),
    }


@enable_ab_test(DEMO_WORKFLOW_V2)
def product(request):
    context = _get_global_context()
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - CommCare (top fold)"
    return render(request, 'pages/commcare/product.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def product_features(request):
    context = _get_global_context()
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - CommCare (top fold)"
    return render(request, 'pages/commcare/product_features.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def pricing(request):
    context = _get_global_context()
    context['feature_groups'] = [g.GROUP for g in feature_groups]
    context['kmq_track_pricing_nav'] = "Clicked Start Trial - Pricing Top"
    return render(request, 'pages/commcare/pricing.html', context)


def research(request):
    return render(request, 'pages/commcare/research.html')


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

@enable_ab_test(DEMO_WORKFLOW_V2)
def commcare_integration(request):
    context = _get_global_context()
    return render(request, 'pages/commcare/commcare_integration.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def commcare_messaging(request):
    context = _get_global_context()
    return render(request, 'pages/commcare/commcare_messaging.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def commcare_onboarding(request):
    context = _get_global_context()
    return render(request, 'pages/commcare/commcare_onboarding.html', context)

@enable_ab_test(DEMO_WORKFLOW_V2)
def monitoring_evaluation(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/commcare/commcare_m&e.html', context)

@enable_ab_test(DEMO_WORKFLOW_V2)
def ict4d(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/commcare/commcare_ict4d.html', context)

@enable_ab_test(DEMO_WORKFLOW_V2)
def vaccine_delivery(request):
    return render(request, 'pages/commcare/vaccine_delivery.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def enterprise(request):
    context = {
        'partners': get_enterprise_partners(),
        'is_inverse_header': True,
    }
    return render(request, 'pages/commcare/enterprise.html', context)

