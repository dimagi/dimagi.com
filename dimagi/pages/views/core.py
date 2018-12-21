from __future__ import absolute_import
from django.shortcuts import render

from dimagi.utils.ab_tests import DEMO_WORKFLOW
from dimagi.utils.decorators import no_index, hide_drift
from dimagi.utils.decorators.enable_ab_test import enable_ab_test
from dimagi.utils.partners import get_logos
from dimagi.data.case_management import longitudinal_data


@enable_ab_test(DEMO_WORKFLOW)
def home(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/home.html', context)


def services(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/services.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


def proposals(request):
    return render(request, 'pages/proposals.html')


def case_management(request):
    context = {
        'table': longitudinal_data.TABLE
    }
    return render(request, 'pages/case_management.html', context)


@no_index
@hide_drift
def referral_commcare(request):
    return render(request, 'pages/referral_commcare.html')


@no_index
def test_500(request):
    return render(request, '500.html')


@no_index
def test_404(request):
    return render(request, '404.html')
