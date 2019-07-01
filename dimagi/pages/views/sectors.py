from __future__ import absolute_import

from django.http import Http404
from django.shortcuts import render


from dimagi.utils.ab_tests import DEMO_WORKFLOW_V2
from dimagi.utils.decorators.enable_ab_test import enable_ab_test
from dimagi.data.sectors import (
    get_sector_by_slug,
    get_sectors_page,
)


def view_all(request):
    sectors = get_sectors_page(1)  # todo pagination
    context = {
        'sectors': sectors,
    }
    return render(request, 'pages/sectors/view_all.html', context)


def view_single(request, slug):
    sector = get_sector_by_slug(slug)
    if not sector:
        raise Http404()
    context = {
        'sector': sector,
    }
    return render(request, 'pages/sectors/view_single.html', context)

@enable_ab_test(DEMO_WORKFLOW_V2)
def maternal_and_child_health(request):
    context = {
        'sector': 'maternal_and_child_health',
    }
    return render(request, 'pages/sectors/maternal_and_child_health.html', context)