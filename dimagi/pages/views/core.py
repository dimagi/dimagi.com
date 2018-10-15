from __future__ import absolute_import
from django.shortcuts import render
from dimagi.utils.decorators import no_index
from dimagi.utils.partners import get_logos
from dimagi.data.case_management import longitudinal_data


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


def proposals(request):
    return render(request, 'pages/proposals.html')


def case_management(request):
    context = {
        'table': longitudinal_data.TABLE
    }
    return render(request, 'pages/case_management.html', context)


@no_index
def test_500(request):
    return render(request, '500.html')


@no_index
def test_404(request):
    return render(request, '404.html')
