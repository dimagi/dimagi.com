from functools import wraps

from django.http import Http404
from django.shortcuts import render
from django.urls import reverse

from dimagi.blog.categories import (
    PRODUCT,
    PARTNERS,
    STAFF,
    ARCHIVE,
    get_category_by_slug,
)
from dimagi.blog.models import BlogPost
from dimagi.utils.decorators import no_index
from dimagi.utils.wordpress_api import get_json


def validate_category(fn):
    @wraps(fn)
    def _validate_category(request, category, *args, **kwargs):
        available_cat = [c.slug for c in [PRODUCT, PARTNERS, STAFF, ARCHIVE]]
        if category not in available_cat:
            raise Http404()
        return fn(request, category, *args, **kwargs)

    return _validate_category


def _get_posts(category, page=None, num_posts=None):
    return [BlogPost(data) for data in get_json(
        'blog/{}'.format(category.slug), page=page, num_posts=num_posts)]


def _get_global_context():
    return {
        'categories': [PRODUCT, PARTNERS, STAFF],
    }


@no_index
def home(request):
    posts = _get_posts(ARCHIVE)
    context = _get_global_context()
    context.update({
        'recent': posts[:2],
        'others': posts[2:],
        'popular': posts[:2],  # todo
    })
    return render(request, 'blog/home.html', context)


@no_index
@validate_category
def archive(request, category, page=None):
    category = get_category_by_slug(category)
    posts = _get_posts(category, page, 20)
    context = _get_global_context()
    page = int(page or 1)
    context.update({
        'category': category,
        'posts': posts,
        'page': page,
    })

    if page > 1:
        previous_url = reverse('blog_archive_page',
                               args=[category.slug, page - 1])
        context['previous_url'] = previous_url

    next_url = reverse('blog_archive_page',
                       args=[category.slug, page + 1])
    context['next_url'] = next_url

    return render(request, 'blog/archive.html', context)


@no_index
def post(request, category, slug):
    category = get_category_by_slug(category)
    _post = get_json('blog/post/{}/'.format(slug))
    if _post.get('not_found'):
        raise Http404()
    if category != ARCHIVE and category.slug != _post['category']:
        raise Http404()
    _post = BlogPost(_post)
    context = _get_global_context()
    context['post'] = _post
    return render(request, 'blog/post.html', context)
