from __future__ import absolute_import
import requests

from dimagi.utils.config import setting
from dimagi.pages.views import blog

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

def get_us_health_json(tags, **kwargs):
    posts = blog._get_posts(blog.ARCHIVE)
    data = search_wordpress(num_posts= posts['total'])
    return data


def get_all_tags():
    from dimagi.pages.models.blog import Tag
    tag_data = get_json('blog/list-tags/')
    tags = [Tag(t) for t in tag_data['tags']]
    return tags


def get_tag_by_id(tag_id, available_tags):
    try:
        tag_id = int(tag_id)
        tags_by_id = {tag.id: tag for tag in available_tags}
        return tags_by_id.get(tag_id)
    except ValueError:
        return None


def get_tag_by_slug(tag_slug, available_tags):
    tags_by_slug = {tag.slug: tag for tag in available_tags}
    return tags_by_slug.get(tag_slug)


def search_wordpress(term=None, category=None, tags=None, page=1, num_posts=None, before=None, after=None):
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

    if num_posts:
        query['num_posts'] = num_posts

    data = requests.post(
        search_url,
        json=query,
        headers=_get_headers()
    )
    return data.json()
