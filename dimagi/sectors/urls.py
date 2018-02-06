from django.conf.urls import url

from dimagi.sectors.views import (
    child_health,
)

urlpatterns = [
    url(r'^child-health/$', child_health,
        name='child_health'),
]
