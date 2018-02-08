from __future__ import absolute_import
from django.shortcuts import render
from dimagi.utils.decorators import no_index


@no_index
def home(request):
    return render(request, 'pages/home.html')


@no_index
def products_commcare(request):
    return render(request, 'pages/products/commcare.html')


@no_index
def services(request):
    return render(request, 'pages/services.html')


@no_index
def pricing_commcare(request):
    return render(request, 'pages/pricing/commcare.html')


@no_index
def pricing_services(request):
    return render(request, 'pages/pricing/services.html')


@no_index
def toolkits(request):
    return render(request, 'pages/toolkits.html')


@no_index
def about(request):
    return render(request, 'pages/about.html')


@no_index
def careers(request):
    return render(request, 'pages/careers.html')


@no_index
def contact(request):
    return render(request, 'pages/contact.html')

