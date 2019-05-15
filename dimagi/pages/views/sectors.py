from __future__ import absolute_import

from django.http import Http404
from django.shortcuts import render

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

def disease_treatment(request):
    context = {
        'sector': 'disease_treatment',
    }
    return render(request, 'pages/sectors/disease_treatment.html', context)


def view_single(request, slug):
    sector = get_sector_by_slug(slug)
    if not sector:
        raise Http404()
    context = {
        'sector': sector,
    }
    return render(request, 'pages/sectors/view_single.html', context)
