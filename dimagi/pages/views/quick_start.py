from django.http import Http404
from django.shortcuts import render

from dimagi.data.quick_start import (
    get_area_by_slug,
)


def view_all(request):
    return render(request, 'pages/quick_start/view_all.html')


def view_single(request, slug):
    area = get_area_by_slug(slug)
    if not area:
        raise Http404()
    context = {
        'area': area,
    }
    return render(request, 'pages/quick_start/view_single.html', context)
