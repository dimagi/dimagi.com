from django.http import Http404
from django.shortcuts import render

from dimagi.data.toolkits import (
    get_tookits_page,
    get_toolkit_by_slug,
)


def view_all(request):
    toolkits = get_tookits_page(1)  # todo pages
    context = {
        'toolkits': toolkits,
    }
    return render(request, 'pages/toolkits/view_all.html', context)


def view_single(request, slug):
    toolkit = get_toolkit_by_slug(slug)
    if not toolkit:
        raise Http404()
    context = {
        'toolkit': toolkit,
    }
    return render(request, 'pages/toolkits/view_single.html', context)
