from __future__ import absolute_import
from django.shortcuts import render

from dimagi.utils.decorators.amp_page_type import set_amp_page_type, AmpPageType
from dimagi.utils.decorators.enable_amp import enable_amp


@enable_amp
@set_amp_page_type(AmpPageType.PILLAR)
def mobile_data_collection(request):
    return render(request, 'pages/pillar/mobile_data_collection.html')
