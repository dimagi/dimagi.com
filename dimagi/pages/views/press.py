from django.shortcuts import render
from django.urls import reverse

from dimagi.data.press import (
    get_press_page,
    TOTAL_PAGES,
)
from dimagi.data.press.outlets import OUTLETS
from dimagi.utils.decorators import no_index


@no_index
def view_all(request, page=None):
    page = int(page or 1)
    press_articles = get_press_page(page)
    context = {
        'press_articles': press_articles,
        'page': page,
        'total_pages': TOTAL_PAGES,
        'outlets': OUTLETS,
    }
    if page > 1:
        previous_url = reverse('press_page', args=[page - 1])
        context['previous_url'] = previous_url

    if page < TOTAL_PAGES:
        next_url = reverse('press_page', args=[page + 1])
        context['next_url'] = next_url

    return render(request, 'pages/press.html', context)
