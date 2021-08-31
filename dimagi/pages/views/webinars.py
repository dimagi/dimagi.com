from django.http import Http404
from django.shortcuts import render

from dimagi.data.case_studies import (
    get_case_study_by_slug,
    get_case_studies_page,
)
from dimagi.utils.hubspot_api import activate_hubspot_cta


def view_all(request):
    studies = get_case_studies_page(1)  # todo other pages
    context = {
        'studies': studies,
    }
    return render(request, 'pages/webinars/view_all.html', context)


def view_single(request, slug):
    study = get_case_study_by_slug(slug)
    if not study:
        raise Http404()
    context = {
        'study': study,
    }
    if study.primary_cta:
        cta_title = f'Case Study: {study.event_tracking_title} ({study.slug})'
        activate_hubspot_cta(request, study.primary_cta, cta_title)
        activate_hubspot_cta(request, study.subnav_cta, f'{cta_title} (Sub Nav)')
    return render(request, 'pages/case_studies/view_single.html', context)
