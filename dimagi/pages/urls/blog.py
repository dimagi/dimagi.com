from django.conf.urls import url
from django.urls import include

from dimagi.pages.views.blog import archive, home, post
from dimagi.pages.views import redirect


archive_urls = [
    url(r'^$', archive,
        name='archive'),
    url(r'^(?P<category>[\w-]+)/$', archive,
        name='archive_category'),
    url(r'^(?P<category>[\w-]+)/page/(?P<page>[\d]+)/$', archive,
        name='archive_page'),
]


blog_urls = [
    url(r'^$', home, name='blog_home'),
    url(r'^archive/', include(archive_urls)),
    url(r'^category/(?P<category>[\w-]+)/$', redirect.blog_category),
    url(r'^tag/(?P<tag>[\w-]+)/$', redirect.blog_tag),
    url(r'^(?P<slug>[\w-]+)/$', post, name='blog_post'),
]
