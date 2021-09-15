from django.conf.urls import url

from dimagi.pages.views.webinars import (
    webinar_home,
    global_me
)


urlpatterns = [
    url(r'^$', webinar_home,
        name='webinar_home'),
    url(r'^Learn-how-to-build-a-global-M&E-system/$', global_me,
        name='global_me'),
]
