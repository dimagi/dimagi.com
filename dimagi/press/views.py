from django.shortcuts import render
from dimagi.press.utils import get_press_page
from dimagi.utils.decorators import no_index


@no_index
def view_all(request):
    press_articles = get_press_page(1)  # todo pages
    context = {
        'press_articles': press_articles,
    }
    return render(request, 'press/press.html', context)
