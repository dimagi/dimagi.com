from django.conf.urls import url

from dimagi.pages.views.team import team, team_member


urlpatterns = [
    url(r'^$', team, name='team'),
    url(r'^(?P<office>[\w-]+)/(?P<slug>[\w-]+)/$',
        team_member, name='team_member'),
]
