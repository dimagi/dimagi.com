from __future__ import absolute_import
from django.conf import settings
from django import template

register = template.Library()

try:
    from static_versions import static_versions
except (ImportError, SyntaxError):
    static_versions = {}


@register.filter
@register.simple_tag
def static(url):
    resource_url = url
    version = static_versions.get(resource_url)
    url = settings.STATIC_CDN + settings.STATIC_URL + url
    is_less = url.endswith('.less')
    if version and not is_less:
        url += "?version=%s" % version
    return url
