from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from dimagi.data.terms import (
    get_terms_by_version,
    get_term_by_slug,
)


def default(request):
    return HttpResponseRedirect(reverse('terms', args=['latest', 'privacy']))


def default_latest(request):
    return HttpResponseRedirect(reverse('terms', args=['latest', 'privacy']))


def default_previous(request):
    return HttpResponseRedirect(reverse('terms', args=['previous', 'privacy']))


def get_terms(request, version, slug=None):
    try:
        if slug is None:
            return HttpResponseRedirect(
                reverse('terms', args=[version, 'privacy'])
            )
        terms = get_terms_by_version(version)
        term = get_term_by_slug(terms, slug)
    except KeyError:
        raise Http404()
    return render(request, 'pages/terms.html', {
        'terms_template': 'data/terms/{}/{}.html'.format(
            term.version,
            term.slug
        ),
        'terms_title': term.title,
        'terms': terms,
        'version': version,
    })
