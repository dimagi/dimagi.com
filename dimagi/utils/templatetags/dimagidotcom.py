from __future__ import absolute_import
from django.conf import settings
from django import template

register = template.Library()

try:
    # todo compile resource_versions
    from resource_versions import resource_versions
except (ImportError, SyntaxError):
    resource_versions = {}


@register.filter
@register.simple_tag
def static(url):
    resource_url = url
    version = resource_versions.get(resource_url)
    url = settings.STATIC_CDN + settings.STATIC_URL + url
    is_less = url.endswith('.less')
    if version and not is_less:
        url += "?version=%s" % version
    return url
