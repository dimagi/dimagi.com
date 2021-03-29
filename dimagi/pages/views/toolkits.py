from django.http import Http404
from django.shortcuts import render

from dimagi.data.toolkits import (
    get_tookits_page,
    get_toolkit_by_slug,
)

from dimagi.utils.hubspot_api import activate_hubspot_cta

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
    if toolkit.primary_cta:
        cta_title = f'Toolkit: {toolkit.event_tracking_title} ({toolkit.slug})'
        activate_hubspot_cta(request, toolkit.primary_cta, cta_title)
        activate_hubspot_cta(request, toolkit.subnav_cta, f'{cta_title} (Sub Nav)')
    return render(request, 'pages/toolkits/view_single.html', context)
