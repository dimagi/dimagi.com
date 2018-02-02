from django.conf.urls import url

from dimagi.blog.views import home, archive, post

urlpatterns = [
    url(r'^$', home,
        name='blog_home'),
    url(r'^(?P<category>[\w-]+)/$', archive,
        name='blog_archive'),
    url(r'^(?P<category>[\w-]+)/page/(?P<page>[\d]+)/$', archive,
        name='blog_archive_page'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', post,
        name='blog_post'),
]
