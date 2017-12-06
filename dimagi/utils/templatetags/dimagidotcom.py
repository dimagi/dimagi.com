from __future__ import absolute_import
import json
from django import template
from django.http import QueryDict
from django.utils.safestring import mark_safe
from dimagi.utils.sass import CDNSassSrcNode
from dimagi.utils.web import json_handler, get_static_url

try:
    from static_versions import static_versions
except (ImportError, SyntaxError):
    static_versions = {}

register = template.Library()


@register.tag(name='sass_src')
def render_sass_src(parser, token):
    return CDNSassSrcNode.handle_token(parser, token)


@register.filter
@register.simple_tag
def static(url):
    """
    Handle the rendering of the static file path and bump it to a CDN if applicable.
    """
    static_url = get_static_url(url)
    version = static_versions.get(url)
    if version:
        static_url = "{}?version={}".format(static_url, version)

    return static_url


def _escape_script_tags(unsafe_str):
    # seriously: http://stackoverflow.com/a/1068548/8207
    return unsafe_str.replace('</script>', '<" + "/script>')


@register.filter
def JSON(obj):
    # json.dumps does not properly convert QueryDict array parameter to json
    if isinstance(obj, QueryDict):
        obj = dict(obj)
    try:
        return mark_safe(_escape_script_tags(json.dumps(obj, default=json_handler)))
    except TypeError as e:
        raise e


@register.filter
def BOOL(obj):
    try:
        obj = obj.to_json()
    except AttributeError:
        pass
    return 'true' if obj else 'false'
