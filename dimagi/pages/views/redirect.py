from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from dimagi.data.blog import categories
from django.shortcuts import redirect


def page(page_slug):
    def _redirect(request):
        return HttpResponsePermanentRedirect(reverse(page_slug))
    return _redirect


def temp_redirect(page_slug):
    def _redirect(request):
        response = redirect(page_slug)
        response.status_code = 307
        return response
    return _redirect


def sector(slug):
    def _redirect(request):
        return HttpResponsePermanentRedirect(reverse('sector', args=[slug]))
    return _redirect


def case_study(slug):
    def _redirect(request):
        return HttpResponsePermanentRedirect(reverse('case_study', args=[slug]))
    return _redirect


def blog(slug):
    def _redirect(request):
        return HttpResponsePermanentRedirect(reverse('blog_post', args=[slug]))
    return _redirect


def team_member(office, slug):
    def _redirect(request):
        return HttpResponsePermanentRedirect(
            reverse('team_member', args=[office, slug])
        )
    return _redirect


def _map_new_categories(category):
    new_mapping = {
        'guest': categories.PARTNERS.slug,
        'from-the-open-source': categories.TECH.slug,
        'dimagineering': categories.TECH.slug,
        'commcare-updates': categories.PRODUCT.slug,
    }
    return new_mapping.get(category, categories.STAFF.slug)


def blog_category(request, category):
    return HttpResponsePermanentRedirect(
        reverse('archive_category', args=[_map_new_categories(category)])
    )


def blog_tag(request, tag):
    return HttpResponsePermanentRedirect(
        reverse('archive_category', args=[_map_new_categories(tag)])
    )


def blog_old_category(request, category):
    return HttpResponsePermanentRedirect(reverse('blog_home'))


def dimagispace(request, year, month):
    return HttpResponsePermanentRedirect(reverse('blog_home'))


def careers_old(request, slug):
    return HttpResponsePermanentRedirect(reverse('careers'))
