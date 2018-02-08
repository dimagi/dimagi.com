import json
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils.translation import ugettext
from django.views.decorators.http import require_http_methods

from dimagi.toolkits.utils import (
    get_tookits_page,
    get_toolkit_by_slug,
)
from dimagi.utils.decorators import no_index


@no_index
def view_all(request):
    toolkits = get_tookits_page(1)  # todo pages
    context = {
        'toolkits': toolkits,
    }
    return render(request, 'toolkits/view_all.html', context)


@no_index
def view_single(request, slug):
    toolkit = get_toolkit_by_slug(slug)
    if not toolkit:
        raise Http404()
    context = {
        'toolkit': toolkit,
    }
    return render(request, 'toolkits/view_single.html', context)


@no_index
@require_http_methods(["POST"])
def download(request, slug):
    toolkit = get_toolkit_by_slug(slug)
    if not toolkit:
        raise Http404()

    email = request.POST.get('email')
    response = {}
    if email:
        response['download_url'] = toolkit.download_url
    else:
        response['error'] = ugettext(
            "An email is required to download this Case Study."
        )
    return HttpResponse(json.dumps(response), content_type="application/json")

