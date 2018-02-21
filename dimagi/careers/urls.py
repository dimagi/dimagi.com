from django.conf.urls import url

from dimagi.careers.views import home, view_job


urlpatterns = [
    url(r'^$', home,
        name='careers'),
    url(r'^job/(?P<job_id>[\d]+)/$', view_job,
        name='careers_job'),
]
