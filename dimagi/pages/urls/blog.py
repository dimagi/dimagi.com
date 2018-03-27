from django.conf.urls import url
from django.urls import include

from dimagi.pages.views.blog import archive, home, post
from dimagi.pages.views import redirect


archive_urls = [
    url(r'^$', archive,
        name='archive'),
    url(r'^page/(?P<page>[\d]+)/$', archive,
        name='archive_page'),
    url(r'^(?P<category>[\w-]+)/$', archive,
        name='archive_category'),
    url(r'^(?P<category>[\w-]+)/page/(?P<page>[\d]+)/$', archive,
        name='archive_category_page'),
]


blog_urls = [
    url(r'^$', home, name='blog_home'),
    url(r'^archive/', include(archive_urls)),
    url(r'^category/(?P<category>[\w-]+)/$', redirect.blog_category),
    url(r'^tag/(?P<tag>[\w-]+)/$', redirect.blog_tag),
    url(r'^write-my-essay-for-me/$', redirect.page('blog_home')),
    url(r'^staff/$', redirect.page('blog_home')),
    url(r'^site-outage/$', redirect.page('blog_home')),
    url(r'^site-outage/$', redirect.page('blog_home')),
    url(r'^service-disruption-of-commcare-hq/$', redirect.page('blog_home')),
    url(r'^planned-commcarehq-downtime-for-maintenance/$', redirect.page('blog_home')),
    url(r'^news/$', redirect.page('blog_home')),
    url(r'^issues-with-recent-case-data-in-reports/$', redirect.page('blog_home')),
    url(r'^how-to-prevent-plagiarism/$', redirect.page('blog_home')),
    url(r'^announcing-dimagi-south-africas-commcare-training-centre/$', redirect.page('blog_home')),
    url(r'^(?P<slug>[\w-]+)/$', post, name='blog_post'),
]
