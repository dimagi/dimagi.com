from __future__ import absolute_import
from django.shortcuts import render


def mobile_data_collection(request):
    return render(request, 'pages/pillar/mobile_data_collection.html')
