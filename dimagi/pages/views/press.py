from django.shortcuts import render
from django.urls import reverse

from dimagi.utils.wordpress_api import (
    search_wordpress,
)

def in_news(request):
    posts = search_wordpress(
            num_posts=4,
            page=1,
            tags=683,
        )
    context = {
        'posts': posts['posts'],
    }
    return render(request, 'pages/press.html', context)

