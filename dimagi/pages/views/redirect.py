from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from dimagi.data.blog import categories


def page(page_slug):
    def _redirect(request):
        return HttpResponsePermanentRedirect(reverse(page_slug))
    return _redirect


def blog(slug):
    def _redirect(request):
        return HttpResponsePermanentRedirect(reverse('blog_post', args=[slug]))
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
    return HttpResponsePermanentRedirect(reverse('blog_home'))
