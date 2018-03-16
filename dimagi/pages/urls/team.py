from django.conf.urls import url

from dimagi.pages.views.team import (
    team,
    team_member,
    about,
)
from dimagi.pages.views import redirect


team_urls = [
    url(r'^$', team, name='team'),
    url(r'^(?P<office>[\w-]+)/(?P<slug>[\w-]+)/$',
        team_member, name='team_member'),
]


about_urls = [
    url(r'^$', about, name='about'),
    url(r'^team/$', redirect.page('team')),
    url(r'^careers/$', redirect.page('careers')),
    url(r'^publications/$', redirect.page('press')),
]
