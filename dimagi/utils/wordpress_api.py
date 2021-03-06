from __future__ import absolute_import
import requests

from dimagi.utils.config import setting

API_URL = setting('WORDPRESS_API_URL', '')
USER_AGENT = setting('WORDPRESS_API_USER_AGENT', '')


def _get_url(item):
    return "{}/{}".format(API_URL.rstrip('/'), item)


def _get_headers():
    return {
        'user-agent': USER_AGENT
    }


def url_filters(content):
    if content:
        content = content.replace(
            'http://dimagi', '//dimagi'
        ).replace(
            'http://www.dimagi.com', 'https://dimagi.wpengine.com'
        ).replace(
            '"/wp-content/', '"//dimagi.wpengine.com/wp-content/'
        )
    return content


def get_json(item, **kwargs):
    data = requests.get(_get_url(item), headers=_get_headers(), params=kwargs)
    return data.json()
