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
from dimagi.utils.wordpress_api import (
    get_json,
    search_wordpress,
    get_all_tags,
    get_tag_by_id,
    get_tag_by_slug,
)

from dimagi.utils.ab_tests import DEMO_WORKFLOW_V2
from dimagi.utils.decorators.enable_ab_test import enable_ab_test


def validate_category(fn):
    @wraps(fn)
    def _validate_category(request, category=None, *args, **kwargs):
        available_cat = [c.slug for c in available_categories]
        if category not in available_cat and category is not None:
            raise Http404()
        return fn(request, category, *args, **kwargs)

    return _validate_category


def process_and_validate_tag(fn):
    @wraps(fn)
    def _validate_tag(request, tag, *args, **kwargs):
        available_tags = get_all_tags()
        request.all_tags = available_tags
        tag_obj = get_tag_by_id(tag, available_tags)
        if tag_obj is None:
            tag_obj = get_tag_by_slug(tag, available_tags)
        if tag_obj is None:
            raise Http404()
        request.tag = tag_obj
        return fn(request, tag, *args, **kwargs)

    return _validate_tag


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


def _get_totals_context(page, total_posts, posts_per_page, num_queried_posts):
    page = int(page or 1)
    total_pages = math.ceil(total_posts / posts_per_page)
    total_previous = (page - 1) * 20
    return {
        'total_posts': total_posts,
        'total_pages': total_pages,
        'from_post': 1 + total_previous,
        'to_post': num_queried_posts + total_previous,
    }


def home(request):
    posts = _get_posts(ARCHIVE)['posts']
    popular = [BlogPost(p) for p in get_json('blog/popular', num_posts=3)['posts']]
    context = _get_global_context()
    context.update({
        'recent': posts[:1],
        'recent_new': posts[1:3],
        'others': posts[3:7],
        'popular': popular,  # todo
    })
    return render(request, 'pages/blog/home.html', context)


@validate_category
def archive(request, category=None, page=None):
    category = get_category_by_slug(category or ARCHIVE.slug)
    posts = _get_posts(category, page, 20)
    context = _get_global_context()
    page = int(page or 1)
    total_posts = int(posts['total'])
    context.update({
        'category': category,
        'posts': posts['posts'],
        'page': page,
    })
    context.update(_get_totals_context(
        page,
        total_posts,
        20,
        len(posts['posts'])
    ))

    if page > 1:
        if category.slug == ARCHIVE.slug:
            previous_url = reverse('archive_page', args=[page - 1])
        else:
            previous_url = reverse(
                'archive_category_page', args=[category.slug, page - 1]
            )
        context['previous_url'] = previous_url

    if page < context['total_pages']:
        if category.slug == ARCHIVE.slug:
            next_url = reverse('archive_page', args=[page + 1])
        else:
            next_url = reverse(
                'archive_category_page', args=[category.slug, page + 1]
            )
        context['next_url'] = next_url

    return render(request, 'pages/blog/archive.html', context)


@process_and_validate_tag
def tag_archive(request, tag, page=None):
    page = int(page or 1)
    search_results = search_wordpress(
        num_posts=20,
        page=page,
        tags=[request.tag.id],
    )
    posts = search_results['posts']

    context = _get_global_context()
    context.update({
        'tag': request.tag,
        'posts': posts,
        'page': page,
    })

    context.update(_get_totals_context(
        page,
        request.tag.total,
        20,
        len(posts)
    ))

    if page > 1:
        context['previous_url'] = reverse('blog_tag_archive_page', args=[tag, page - 1])

    if page < context['total_pages']:
        context['next_url'] = reverse('blog_tag_archive_page', args=[tag, page + 1])

    return render(request, 'pages/blog/archive.html', context)


def post(request, slug):
    _post = get_json('blog/post/{}/'.format(slug))

    if _post.get('not_found'):
        raise Http404()

    _post = BlogPost(_post)
    context = _get_global_context()
    context['post'] = _post
    return render(request, 'pages/blog/post.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def mobile_data_collection_blog_post(request):
    template= "pages/blog/mobile_blog.html"
    return render(request, template)
