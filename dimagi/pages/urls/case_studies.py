from django.conf.urls import url

from dimagi.pages.views.case_studies import view_all, view_single


urlpatterns = [
    url(r'^$', view_all,
        name='case_studies'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='case_study'),
]
