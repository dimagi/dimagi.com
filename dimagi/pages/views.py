from __future__ import absolute_import
from django.shortcuts import render
from dimagi.utils.decorators import no_index


@no_index
def home(request):
    return render(request, 'pages/home.html')


@no_index
def products(request):
    return render(request, 'pages/products.html')
