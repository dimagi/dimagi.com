from django.http import Http404
from django.shortcuts import render

from dimagi.data.case_studies import (
    get_case_study_by_slug,
    get_case_studies_page,
)


def view_all(request):
    studies = get_case_studies_page(1)  # todo other pages
    context = {
        'studies': studies,
    }
    return render(request, 'pages/case_studies/view_all.html', context)


def view_single(request, slug):
    study = get_case_study_by_slug(slug)
    if not study:
        raise Http404()
    context = {
        'study': study,
    }
    return render(request, 'pages/case_studies/view_single.html', context)
