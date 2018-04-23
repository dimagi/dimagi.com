from django.conf.urls import url

from dimagi.pages.views.terms import privacy, privacy_new, eula, subscription


urlpatterns = [
    url(r'^$', privacy,
        name='privacy_policy'),
    url(r'^eula/$', eula,
        name='eula'),
    url(r'^subscription/$', subscription,
        name='subscription_agreement'),

    url(r'^latest/privacy/$', privacy_new,
        name='latest_privacy_policy'),
]
