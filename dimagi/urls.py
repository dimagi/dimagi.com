from __future__ import absolute_import
from django.conf.urls import url, include
import dimagi.pages.views as pages
from dimagi.pages.views import commcare
from dimagi.pages.views import team
from dimagi.pages.urls import blog


urlpatterns = [
    url(r'^$', pages.home,
        name='home'),
    url(r'^services/$', pages.services,
        name='services'),
    url(r'^contact/$', pages.contact,
        name='contact'),
    url(r'^certified-partners/$', commcare.partners,
        name='partner_program'),
    url(r'^about/$', team.about,
        name='about'),
    url(r'^commcare/',
        include('dimagi.pages.urls.commcare')),
    url(r'^case-studies/',
        include('dimagi.pages.urls.case_studies')),
    url(r'^toolkits/',
        include('dimagi.pages.urls.toolkits')),
    url(r'^blog/',
        include(blog.blog_urls)),
    url(r'^archive/',
        include(blog.archive_urls)),
    url(r'^sectors/',
        include('dimagi.pages.urls.sectors')),
    url(r'^team/',
        include('dimagi.pages.urls.team')),
    url(r'^careers/',
        include('dimagi.pages.urls.careers')),
    url(r'^press/',
        include('dimagi.pages.urls.press')),
    url(r'^policy/',
        include('dimagi.pages.urls.policies')),
]
