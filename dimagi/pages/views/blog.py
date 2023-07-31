from functools import wraps
import math
import urllib.parse

from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import ugettext

from dimagi.data.blog import (
    available_categories,
    nav_categories,
    get_category_by_slug,
    ARCHIVE,
    COMMCARE_PROVIDER,
)
from dimagi.pages.models.blog import BlogPost
from dimagi.utils.request_helpers import (
    get_selected_tags_from_request,
    get_search_term_from_request,
)
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


def populate_tags_in_request(fn):
    @wraps(fn)
    def _populate_tags(request, *args, **kwargs):
        request.tags = get_all_tags()
        return fn(request, *args, **kwargs)

    return _populate_tags


def process_and_validate_tag(fn):
    @wraps(fn)
    def _validate_tag(request, tag, *args, **kwargs):
        tag_obj = get_tag_by_id(tag, request.tags)
        if tag_obj is None:
            tag_obj = get_tag_by_slug(tag, request.tags)
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

def _get_commcare_providers(category, page=None, num_posts=None):
    post_data = get_json(
        'commcare-providers', page=page, num_posts=20)
    return {
        'posts': [BlogPost(data) for data in post_data['posts']],
        'total': post_data['total'],
    }


def _get_global_context(request):
    categories = [{
        'name': ugettext("All Categories"),
        'slug': 'all',
        'url': reverse('archive'),
    }]
    categories.extend([{
        'name': ugettext(c.name),
        'slug': c.slug,
        'url': reverse('archive_category', args=(c.slug,)),
    } for c in nav_categories])
    return {
        'categories': nav_categories,
        'blog_filters': {
            'categories': categories,
            'tags': [{
                'name': t.name,
                'id': t.id,
            } for t in request.tags],
        }
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


@populate_tags_in_request
def home(request):
    posts = _get_posts(ARCHIVE)['posts']
    popular = [BlogPost(p) for p in get_json('blog/popular', num_posts=3)['posts']]
    context = _get_global_context(request)
    context.update({
        'recent': posts[:1],
        'recent_new': posts[1:3],
        'others': posts[3:7],
        'popular': popular,  # todo
    })
    return render(request, 'pages/blog/home.html', context)


@populate_tags_in_request
@validate_category
def archive(request, category=None, page=None):
    print('-------------------------------------------------')
    print(request)
    print('+++++++++++++++++++++++++++++++++++++++++')
    search_term = get_search_term_from_request(request)
    tags = get_selected_tags_from_request(request)
    search_category = category
    category = get_category_by_slug(category or ARCHIVE.slug)

    context = _get_global_context(request)
    page = int(page or 1)
    max_posts = 20
    append_to_url = ''

    if search_term or tags:
        search_tag_ids = [t.id for t in tags] if tags is not None else None
        search_tag_names = [f'"{t.name}"' for t in tags] if tags is not None else None
        url_query = {
            's': search_term or '',
            't': ','.join([str(t) for t in search_tag_ids]) if search_tag_ids else '',
        }
        append_to_url = f"?{urllib.parse.urlencode(url_query)}"
        posts = search_wordpress(
            num_posts=max_posts,
            page=page,
            term=search_term,
            category=search_category,
            tags=search_tag_ids,
        )
        context.update({
            'is_search_page': True,
            'existing_filters': {
                'term': search_term,
                'tags': search_tag_ids,
                'category': search_category or 'all',
            },
            'tag_summary': ', '.join(search_tag_names) if search_tag_names else None,
        })
        total_posts = len(posts['posts'])
        if total_posts == max_posts:
            # we can't easily get the total posts for a search page right now,
            # but if it fills up, assume there might be a next page
            total_posts = total_posts * page + 1
    else:
        posts = _get_posts(category, page, max_posts)
        total_posts = int(posts['total'])
    context.update(_get_totals_context(
        page,
        total_posts,
        max_posts,
        len(posts['posts'])
    ))

    context.update({
        'category': category,
        'posts': posts['posts'],
        'page': page,
    })

    if page > 1:
        if category.slug == ARCHIVE.slug:
            previous_url = reverse('archive_page', args=[page - 1])
        else:
            previous_url = reverse(
                'archive_category_page', args=[category.slug, page - 1]
            )
        context['previous_url'] = previous_url + append_to_url

    if page < context['total_pages']:
        if category.slug == ARCHIVE.slug:
            next_url = reverse('archive_page', args=[page + 1])
        else:
            next_url = reverse(
                'archive_category_page', args=[category.slug, page + 1]
            )
        context['next_url'] = next_url + append_to_url
    
    return render(request, 'pages/blog/archive.html', context)


@populate_tags_in_request
@process_and_validate_tag
def tag_archive(request, tag, page=None):
    page = int(page or 1)
    search_results = search_wordpress(
        num_posts=20,
        page=page,
        tags=[request.tag.id],
    )
    posts = search_results['posts']

    context = _get_global_context(request)
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


@populate_tags_in_request
def post(request, slug):
    post_data = get_json('blog/post/{}/'.format(slug))

    if post_data.get('not_found'):
        raise Http404()

    blog_post = BlogPost(post_data)

    related_posts_data = search_wordpress(
        num_posts=3,
        category=blog_post.category.slug
    )
    related_posts = [BlogPost(p) for p in related_posts_data['posts']]

    context = _get_global_context(request)
    context.update({
        'post': blog_post,
        'related_posts': related_posts,
    })
    context['post'] = blog_post
    return render(request, 'pages/blog/post.html', context)


@enable_ab_test(DEMO_WORKFLOW_V2)
def mobile_data_collection_blog_post(request):
    template= "pages/blog/mobile_blog.html"
    return render(request, template)
