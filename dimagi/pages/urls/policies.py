from django.conf.urls import url

from dimagi.pages.views.policies import privacy, eula, subscription


urlpatterns = [
    url(r'^$', privacy,
        name='privacy_policy'),
    url(r'^eula/$', eula,
        name='eula'),
    url(r'^subscription/$', subscription,
        name='subscription_agreement'),
]
