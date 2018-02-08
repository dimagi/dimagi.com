from __future__ import absolute_import

from django.http import Http404
from django.shortcuts import render

from dimagi.sectors.utils import get_sector_by_slug
from dimagi.utils.decorators import no_index


@no_index
def view_single(request, slug):
    sector = get_sector_by_slug(slug)
    if not sector:
        raise Http404()
    context = {
        'sector': sector,
    }
    return render(request, 'sectors/view_single.html', context)
