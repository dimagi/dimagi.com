from django.shortcuts import render
from dimagi.utils.decorators import no_index


@no_index
def home(request):
    return render(request, 'home.html')


