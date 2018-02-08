from django.conf.urls import url

from dimagi.case_studies.views import view_all, view_single, download

urlpatterns = [
    url(r'^$', view_all,
        name='case_studies'),
    url(r'^(?P<slug>[\w-]+)/$', view_single,
        name='case_study'),
    url(r'^(?P<slug>[\w-]+)/download/$', download,
        name='case_study_download'),
]
