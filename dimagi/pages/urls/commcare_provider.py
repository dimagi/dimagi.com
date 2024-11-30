from django.conf.urls import url
from django.urls import include

from dimagi.pages.views.commcare_provider import (
    archive,
    Provider_home,
)
from dimagi.pages.views import redirect


archive_provider_urls = [
    url(r'^$', archive,
        name='archive'),
]


provider_urls = [
    url(r'^$', Provider_home, name='Commcare_provider'),
]
def get_provider_urls(): 
    print('Request printed _____+++++')
    return provider_urls