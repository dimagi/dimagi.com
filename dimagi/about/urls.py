from django.conf.urls import url

from dimagi.about.views import home, team

urlpatterns = [
    url(r'^$', home, name='about'),
    url(r'^team/$', team, name='about_team'),
]
