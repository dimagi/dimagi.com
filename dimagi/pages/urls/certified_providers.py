from django.conf.urls import url
from django.urls import include

from dimagi.pages.views.certified_providers import (
    home,
)
from dimagi.pages.views import redirect


certified_providers_urls = [
    url(r'^$', home, name='commcareproviders'),
    
]
