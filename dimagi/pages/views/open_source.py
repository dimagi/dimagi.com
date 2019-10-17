from django.shortcuts import render

from dimagi.utils.decorators import no_index


@no_index
def open_source_home(request):
    return render(request, 'pages/open_source/open_source_home.html')
