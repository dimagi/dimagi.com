from functools import wraps
import math

from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from dimagi.data.blog import (
    available_categories,
    nav_categories,
    get_category_by_slug,
    ARCHIVE,
)
from dimagi.pages.models.blog import BlogPost
from dimagi.utils.decorators import no_index, hide_drift
from dimagi.utils.wordpress_api import get_json


def validate_category(fn):
    @wraps(fn)
    def _validate_category(request, category=None, *args, **kwargs):
        available_cat = [c.slug for c in nav_categories]
        if category not in available_cat and category is not None:
            raise Http404()
        return fn(request, category, *args, **kwargs)

    return _validate_category


def _get_posts(category, page=None, num_posts=None):
    post_data = get_json(
        'blog/{}'.format(category.slug), page=page, num_posts=num_posts)
    return {
        'posts': [BlogPost(data) for data in post_data['posts']],
        'total': post_data['total'],
    }


def _get_global_context():
    return {
        'categories': nav_categories,
    }


@no_index
@hide_drift
def home(request):
    posts = _get_posts(ARCHIVE)['posts']
    popular = [BlogPost(p) for p in get_json('blog/popular', num_posts=2)['posts']]
    context = _get_global_context()
    context.update({
        'recent': posts[:2],
        'others': posts[2:],
        'popular': popular,  # todo
    })
    return render(request, 'pages/blog/home.html', context)


@no_index
@hide_drift
@validate_category
def archive(request, category=None, page=None):
    category = get_category_by_slug(category or 'archive')
    posts = _get_posts(category, page, 20)
    context = _get_global_context()
    page = int(page or 1)
    total_posts = int(posts['total'])
    total_pages = math.ceil(total_posts / 20)
    total_previous = (page - 1) * 20
    context.update({
        'category': category,
        'posts': posts['posts'],
        'page': page,
        'total_posts': total_posts,
        'total_pages': total_pages,
        'from_post': 1 + total_previous,
        'to_post': len(posts['posts']) + total_previous,
    })

    if page > 1:
        previous_url = reverse('archive_page',
                               args=[category.slug, page - 1])
        context['previous_url'] = previous_url

    if page < total_pages:
        next_url = reverse('archive_page',
                           args=[category.slug, page + 1])
        context['next_url'] = next_url

    return render(request, 'pages/blog/archive.html', context)


@no_index
@hide_drift
def post(request, slug):
    _post = get_json('blog/post/{}/'.format(slug))

    if _post.get('not_found'):
        raise Http404()

    _post = BlogPost(_post)
    context = _get_global_context()
    context['post'] = _post
    return render(request, 'pages/blog/post.html', context)
