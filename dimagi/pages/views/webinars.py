from __future__ import absolute_import

from django.http import HttpResponse
from django.shortcuts import render

from dimagi.utils.ab_tests import DEMO_WORKFLOW_V2
from dimagi.utils.decorators.enable_ab_test import enable_ab_test
from dimagi.utils.partners import get_logos
from dimagi.utils.enterprise_partners import get_enterprise_partners
from dimagi.data.commcare.pricing import feature_groups
from dimagi.utils.pdf.pricing import get_pricing_pdf


@enable_ab_test(DEMO_WORKFLOW_V2)
def webinar_home(request):
    return render(request, 'pages/webinars/view_all.html')


@enable_ab_test(DEMO_WORKFLOW_V2)
def global_me(request):
    return render(request, 'pages/webinars/global_me.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def data_already(request):
    return render(request, 'pages/webinars/data_already.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def optimize(request):
    return render(request, 'pages/webinars/optimize.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def interoperability(request):
    return render(request, 'pages/webinars/interoperability.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def adapt(request):
    return render(request, 'pages/webinars/adapt.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def new_function(request):
    return render(request, 'pages/webinars/new_function.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def data_clean(request):
    return render(request, 'pages/webinars/data_clean.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def remote(request):
    return render(request, 'pages/webinars/remote.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def covid19(request):
    return render(request, 'pages/webinars/covid19.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def power_bi(request):
    return render(request, 'pages/webinars/power_bi.html')

