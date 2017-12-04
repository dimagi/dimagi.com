from __future__ import absolute_import
from django.conf import settings
from django import template
from sass_processor.templatetags.sass_tags import SassSrcNode

from dimagi.utils.sass import CDNSassProcessor

try:
    from static_versions import static_versions
except (ImportError, SyntaxError):
    static_versions = {}

register = template.Library()


class CDNSassSrcNode(SassSrcNode):
    def __init__(self, path):
        self.sass_processor = CDNSassProcessor(path)


@register.tag(name='sass_src')
def render_sass_src(parser, token):
    return CDNSassSrcNode.handle_token(parser, token)


@register.filter
@register.simple_tag
def static(url):
    """
    Handle the rendering of the static file path and bump it to a CDN if applicable.
    """
    static_url = settings.STATIC_CDN + settings.STATIC_URL + url

    version = static_versions.get(url)
    if version:
        static_url = "{}?version={}".format(static_url, version)

    return static_url
