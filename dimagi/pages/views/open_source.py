from django.shortcuts import render

from dimagi.utils.decorators import no_index

from dimagi.data.open_source.pricing import feature_groups
from dimagi.utils.partners import get_logos


def _get_global_context():
    return {
        'partners': get_logos(),
    }


@no_index
def open_source_home(request):
    return render(request, 'pages/open_source/open_source_home.html')

@no_index
def open_source_hosting(request):
    context = _get_global_context()
    context['feature_groups'] = [g.GROUP for g in feature_groups]
    return render(request, 'pages/open_source/open_source_hosting.html', context)

