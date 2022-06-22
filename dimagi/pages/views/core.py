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
from dimagi.utils.covid_partners import get_us_covid_partners
from dimagi.utils.services import get_service_partners
from dimagi.data.case_management import longitudinal_data

from dimagi.pages.views import blog
from dimagi.utils.wordpress_api import get_json
from dimagi.pages.models.partners import latestPartners


@enable_ab_test(DEMO_WORKFLOW_V2)
def home(request):
    context = {
        'partners': get_logos(),
        'is_inverse_header': True,
    }
    return render(request, 'pages/home.html', context)


def services(request):
    context = {
        'partners': get_service_partners(),
    }
    return render(request, 'pages/services.html', context)

def india(request):
    return render(request, 'pages/india.html')



def partners(request):
    _latest = get_json("blog/latest-partners")
    _partners_count= _latest["total"]
    _latest = latestPartners(_latest["posts"][:2])
    context = {
        'partners': get_logos(),
        'latest_partners': _latest,
        'partners_count': _partners_count
    }
    return render(request, 'pages/partners.html', context)


def covid_19(request):
    context = {
        'posts': get_json("blog/covid-19")['posts'][:4],
    }
    return render(request, 'pages/covid_19.html', context)


def us_covid_19(request):
    context = {
        'partners': get_us_covid_partners(),
        'posts': get_json("blog/covid-19")['posts'][:4],
    }
    return render(request, 'pages/us_covid_19.html', context)


def resources(request):
    posts = blog._get_posts(blog.ARCHIVE)['posts']
    context = {
        'posts': posts[:3],
    }
    return render(request, 'pages/resources.html', context)


def research_and_data(request):
    return render(request, 'pages/research_and_data.html')


def contact(request):
    return render(request, 'pages/contact.html')


def awards(request):
    _post = get_json('blog/post/dimagi-awards/')
    context = {
        'content': _post['content']
    }
    return render(request, 'pages/awards.html', context)


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
