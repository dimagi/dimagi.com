from django.conf.urls import url
from django.urls import include

from dimagi.pages.views.certified_providers import (
    partners,
)
from dimagi.pages.views import redirect


partners_urls = [
    url(r'^$', partners, name='partners'),
    
]
