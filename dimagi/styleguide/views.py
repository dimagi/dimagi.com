from __future__ import absolute_import
from django.shortcuts import render

from dimagi.utils.decorators import hide_drift, no_index


@no_index
@hide_drift
def home(request):
    return render(request, 'styleguide/home.html')


@no_index
@hide_drift
def sizes(request):
    return render(request, 'styleguide/sizes.html')


@no_index
@hide_drift
def grid(request):
    return render(request, 'styleguide/grid.html')


@no_index
@hide_drift
def colors(request):
    return render(request, 'styleguide/colors.html')
