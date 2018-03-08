from __future__ import absolute_import
from django.shortcuts import render
from dimagi.utils.decorators import no_index
from dimagi.utils.partners import get_logos


@no_index
def home(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/home.html', context)


@no_index
def services(request):
    context = {
        'partners': get_logos(),
    }
    return render(request, 'pages/services.html', context)


@no_index
def contact(request):
    return render(request, 'pages/contact.html')

