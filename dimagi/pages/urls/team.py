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
    url(r'^team/africa/kieran/$', redirect.page('team')),
    url(r'^team/india/stella/$', redirect.team_member('india', 'stella')),
    url(r'^team/india/sravan-reddy/$', redirect.team_member('india', 'sravan-reddy')),
    url(r'^team/india/sravan-reddy/$', redirect.team_member('india', 'sravan-reddy')),
    url(r'^team/boston/vikram/$', redirect.team_member('usa', 'vikram')),
    url(r'^team/boston/neal/$', redirect.team_member('usa', 'neal')),
    url(r'^team/africa/mohini-bhavsar/$', redirect.team_member('west-africa', 'mohini-bhavsar')),
    url(r'^careers/$', redirect.page('careers')),
    url(r'^careers/(?P<slug>[\w-]+)/$', redirect.careers_old),
    url(r'^publications/$', redirect.page('press')),
    url(r'^clients/$', redirect.page('home')),
]
