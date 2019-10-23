from __future__ import absolute_import

from django.http import Http404
from django.shortcuts import render

from dimagi.utils.ab_tests import DEMO_WORKFLOW_V2
from dimagi.utils.decorators.enable_ab_test import enable_ab_test

from dimagi.data.sectors import (
    get_sector_by_slug,
    get_sectors_page,
)

def view_single(request, slug):
    sector = get_sector_by_slug(slug)
    if not sector:
        raise Http404()
    context = {
        'sector': sector,
    }
    return render(request, 'pages/sectors/view_single.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def view_all(request):
    sectors = get_sectors_page(1)  # todo pagination
    context = {
        'sectors': sectors,
    }
    return render(request, 'pages/sectors/view_all.html', context)
  

@enable_ab_test(DEMO_WORKFLOW_V2)
def agriculture_extension_programs(request):
    context = {
        'sector': 'agriculture_extension_programs',
    }
    return render(request, 'pages/sectors/agriculture_extension_programs.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def agriculture_finance(request):
    context = {
        'sector': 'agriculture_finance',
    }
    return render(request, 'pages/sectors/agriculture_finance.html', context)
  
  
@enable_ab_test(DEMO_WORKFLOW_V2)
def sector_reproductive_health(request):
    return render(request, 'pages/sectors/reproductive_health.html')
  
  
@enable_ab_test(DEMO_WORKFLOW_V2)
def nutrition_programs(request):
    context = {
        'sector': 'nutrition_programs',
    }
    return render(request, 'pages/sectors/nutrition_programs.html', context)

  
@enable_ab_test(DEMO_WORKFLOW_V2)
def disease_treatment(request):
    context = {
        'sector': 'disease_treatment',
    }
    return render(request, 'pages/sectors/disease_treatment.html', context)

  
@enable_ab_test(DEMO_WORKFLOW_V2)
def maternal_and_child_health(request):
    context = {
        'sector': 'maternal_and_child_health',
    }
    return render(request, 'pages/sectors/maternal_and_child_health.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def education(request):
    context = {
        'sector': 'education',
    }
    return render(request, 'pages/sectors/education.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def small_businesses(request):
    context = {
        'sector': 'small_businesses',
    }
    return render(request, 'pages/sectors/small_businesses.html', context)

  
@enable_ab_test(DEMO_WORKFLOW_V2)
def programmatic_research(request):
    context = {
        'sector': 'programmatic_research',
    }
    return render(request, 'pages/sectors/programmatic_research.html', context)
