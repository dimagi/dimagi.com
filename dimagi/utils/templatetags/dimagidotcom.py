from __future__ import absolute_import
import json
from django import template
from urllib.parse import quote
from django.http import QueryDict
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from compressor.templatetags.compress import compress as original_compress
from sass_processor.templatetags.sass_tags import SassSrcNode
from dimagi.utils.web import json_handler, get_static_url

try:
    from static_versions import static_versions
except (ImportError, SyntaxError):
    static_versions = {}

register = template.Library()


@register.tag(name='sass_src')
def render_sass_src(parser, token):
    return SassSrcNode.handle_token(parser, token)


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


@register.filter
def JOIN(value, arg):
    return arg.join(value)


@register.tag
def compress(parser, token):
    return original_compress(parser, token)


def _render_social_link(share_url, icon):
    return mark_safe(render_to_string("partials/social_link.html", {
        'share_url': share_url,
        'icon': icon,
    }))


@register.simple_tag
def twitter_link(url, text=None, hashtags=None):
    """
    Renders a link for sharing via twitter, including icon.
    :param url - the url to share
    :param text - (optional) the text / title to share
    :param hashtags - (optional) string of hashtags separated by commas
    """
    hashtags = quote(hashtags) or "idt4d,dimagi,MobileDataCollection"

    share_url = (
        "https://twitter.com/share?"
        "url={url}&"
        "via=dimagi&"
        "hashtags={hashtags}&"
        "text={text}&".format(
            url=quote(url).replace('/', '%2F'),
            hashtags=hashtags.replace(',', '%2C'),
            text=quote(text or ""),
        ))

    icon = "svg/social/twitter.html"

    return _render_social_link(share_url, icon)


@register.simple_tag
def facebook_link(url):
    """
    Renders a link for sharing via facebook, including icon.
    :param url - the url to share
    """

    share_url = (
        "https://www.facebook.com/sharer.php?"
        "u={url}".format(
            url=quote(url).replace('/', '%2F'),
        ))

    icon = "svg/social/facebook.html"

    return _render_social_link(share_url, icon)


@register.simple_tag
def linkedin_link(url):
    """
    Renders a link for sharing via linkedIn, including icon.
    :param url - the url to share
    """

    share_url = (
        "https://www.linkedin.com/cws/share?"
        "url={url}".format(
            url=quote(url).replace('/', '%2F'),
        ))

    icon = "svg/social/linkedin.html"

    return _render_social_link(share_url, icon)
