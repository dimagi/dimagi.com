from __future__ import absolute_import

import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from dimagi.utils.ab_tests import DEMO_WORKFLOW_V2
from dimagi.utils.decorators import no_index, hide_drift
from dimagi.utils.decorators.enable_ab_test import enable_ab_test
from dimagi.utils.friendbuy_api import get_share
from dimagi.utils.hubspot_api import update_contact
from dimagi.utils.partners import get_logos
from dimagi.data.case_management import longitudinal_data


@enable_ab_test(DEMO_WORKFLOW_V2)
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

def partners(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/partners.html', context)


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


@require_http_methods(["POST"])
@no_index
def update_referral_status(request):
    share_id = request.POST.get('id')
    share_info = get_share(share_id)
    email = share_info.get('sharer', {}).get('email')
    referral_code = share_info.get('referral_code')
    update_req = update_contact(email, [
        ('referral_customer', 'Yes'),
        ('referral_code_email', referral_code),
    ])
    return HttpResponse(json.dumps({"status": update_req.status_code}),
                        content_type="application/json")


@no_index
def test_500(request):
    return render(request, '500.html')


@no_index
def test_404(request):
    return render(request, '404.html')


def focus_placeholder(request):
    return HttpResponseRedirect("http://focusmdm.com/")
