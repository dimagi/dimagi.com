from django.conf.urls import url

from dimagi.pages.views.webinars import (
    webinar_home,
    global_me,
    data_already,
    optimize,
    interoperability,
    adapt,
    new_function,
    data_clean,
    remote,
    covid19,
    power_bi,
)


urlpatterns = [
    url(r'^$', webinar_home,
        name='webinar_home'),
    url(r'^Learn-how-to-build-a-global-M&E-system/$', global_me,
        name='global_me'),
    url(r'^Learning-from-the-data-you-already-have/$', data_already,
        name='data_already'),
    url(r'^Optimize-your-global-rollout-of-CommCare/$', optimize,
        name='optimize'),
    url(r'^what-interoperability-actually-means/$', interoperability,
        name='interoperability'),
    url(r'^Adapting-Your-App-for-COVID-19/$', adapt,
        name='adapt'),
    url(r'^Adding-New-Functionality-to-Your-CommCare-Application/$', new_function,
        name='new_function'),
    url(r'^Data-Cleaning-and-Management-with-CommCare/$', data_clean,
        name='data_clean'),
    url(r'^Remote-Program-Monitoring-with-CommCare/$', remote,
        name='remote'),
    url(r'^CommCare-for-COVID-19-Response/$', covid19,
        name='covid19'),
    url(r'^Power-BI-Dashboards-for-Monitoring-&-Evaluation/$', power_bi,
        name='power_bi'),
]
