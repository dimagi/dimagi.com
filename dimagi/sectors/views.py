from __future__ import absolute_import
from django.shortcuts import render
from dimagi.utils.decorators import no_index


@no_index
def child_health(request):
    return render(request, 'sectors/child_health.html')
