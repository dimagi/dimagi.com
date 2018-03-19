from django.http import Http404
from django.shortcuts import render

from dimagi.pages.models.team import Employee, Office
from dimagi.utils.wordpress_api import get_json


def _get_management():
    exec = get_json('team/exec')
    return sorted(
        [Employee(e) for e in exec],
        key=lambda x: int(x.order_exec),
        reverse=False
    )


def _get_offices():
    offices = get_json('team')
    return [Office(o) for o in offices]


def _get_member(slug):
    member = get_json('team/member/{}'.format(slug))
    if not member.get('not_found'):
        return Employee(member)


def about(request):
    context = {
        'management': _get_management(),
    }
    return render(request, 'pages/about.html', context)


def team(request):
    context = {
        'offices': _get_offices(),
    }
    return render(request, 'pages/team/team.html', context)


def team_member(request, office, slug):
    member = _get_member(slug)
    if not member:
        raise Http404()
    if member.office != office:
        raise Http404()
    context = {
        'employee': member,
    }
    return render(request, 'pages/team/member.html', context)
