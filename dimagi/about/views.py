from django.shortcuts import render

from dimagi.about.models import Employee, Office
from dimagi.utils.decorators import no_index
from dimagi.utils.wordpress_api import get_json


def _get_management():
    exec = get_json('team/exec')
    return [Employee(e) for e in exec]


def _get_offices():
    offices = get_json('team')
    return [Office(o) for o in offices]


@no_index
def home(request):
    context = {
        'management': _get_management(),
    }
    return render(request, 'about/about.html', context)


@no_index
def team(request):
    context = {
        'offices': _get_offices(),
    }
    return render(request, 'about/team.html', context)
