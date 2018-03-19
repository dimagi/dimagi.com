from __future__ import absolute_import
from django.shortcuts import render
from dimagi.utils.decorators import no_index
from dimagi.utils.partners import get_logos


def home(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/home.html', context)


def services(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/services.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


@no_index
def test_500(request):
    return render(request, '500.html')


@no_index
def test_404(request):
    return render(request, '404.html')

