from django.shortcuts import render
from django.urls import reverse

from dimagi.utils.wordpress_api import get_json


def in_news(request):
    context = {
        'posts': get_json("blog/in-the-news")['posts'][:4],
    }
    return render(request, 'pages/press.html', context)

