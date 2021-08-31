from __future__ import absolute_import
import requests

from dimagi.utils.config import setting

API_URL = setting('WORDPRESS_API_URL', '')
USER_AGENT = setting('WORDPRESS_API_USER_AGENT', '')


class PostCategory(object):
    STAFF = 'staff'
    PARTNERS = 'partners'
    TECH = 'tech'
    PRODUCT = 'product'


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


def search_wordpress(term=None, category=None, tags=None, page=1, before=None, after=None):
    search_url = _get_url('blog/search/')
    query = {
        'page': page,
    }

    if term:
        query['s'] = term

    if category:
        query['category'] = category

    if tags:
        query['tags'] = tags

    if before:
        query['before'] = before

    if after:
        query['after'] = after

    data = requests.post(
        search_url,
        json=query,
        headers=_get_headers()
    )
    return data.json()
