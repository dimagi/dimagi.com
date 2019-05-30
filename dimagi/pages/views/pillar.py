from __future__ import absolute_import
from django.shortcuts import render

from dimagi.utils.ab_tests import DEMO_WORKFLOW_V2
from dimagi.utils.decorators.amp_page_type import set_amp_page_type, AmpPageType
from dimagi.utils.decorators.enable_ab_test import enable_ab_test
from dimagi.utils.decorators.enable_amp import enable_amp


@enable_amp
@set_amp_page_type(AmpPageType.PILLAR)
def mobile_data_collection(request):
    return render(request, 'pages/pillar/mobile_data_collection.html')

@enable_ab_test(DEMO_WORKFLOW_V2)
def data_collection(request):
    return render(request, 'pages/pillar/data_collection.html')
