import json

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils.translation import ugettext
from django.views.decorators.http import require_http_methods

from dimagi.data.case_studies import (
    get_case_study_by_slug,
    get_case_studies_page,
)
from dimagi.utils.decorators import no_index


@no_index
def view_all(request):
    studies = get_case_studies_page(1)  # todo other pages
    context = {
        'studies': studies,
    }
    return render(request, 'pages/case_studies/view_all.html', context)


@no_index
def view_single(request, slug):
    study = get_case_study_by_slug(slug)
    if not study:
        raise Http404()
    context = {
        'study': study,
    }
    return render(request, 'pages/case_studies/view_single.html', context)


@no_index
@require_http_methods(["POST"])
def download(request, slug):
    study = get_case_study_by_slug(slug)
    if not study:
        raise Http404()

    email = request.POST.get('email')
    response = {}
    if email:
        response['download_url'] = study.download_url
    else:
        response['error'] = ugettext(
            "An email is required to download this Case Study."
        )
    return HttpResponse(json.dumps(response), content_type="application/json")

