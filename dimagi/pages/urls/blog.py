from django.conf.urls import url

from dimagi.pages.views.blog import archive, home, post


archive_urls = [
    url(r'^$', archive,
        name='archive'),
    url(r'^(?P<category>[\w-]+)/$', archive,
        name='archive_category'),
    url(r'^(?P<category>[\w-]+)/page/(?P<page>[\d]+)/$', archive,
        name='archive_page'),
]


blog_urls = [
    url(r'^$', home,
        name='blog_home'),
    url(r'^(?P<slug>[\w-]+)/$', post,
        name='blog_post'),
]
