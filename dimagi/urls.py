from __future__ import absolute_import
from django.conf.urls import url, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

import dimagi.pages.views as pages
from dimagi.pages.sitemaps import (
    BlogPostSitemap,
    MainViewSitemap,
    BlogArchiveCategorySitemap,
    SectorSitemap,
    CaseStudySitemap,
    ToolkitSitemap,
    JobsSitemap,
    TeamMemberSitemap,
    TermsSitemap,
    QuickStartSitemap,
)
from dimagi.pages.urls.redirect import redirect_urlpatterns
from dimagi.pages.views import commcare, redirect
from dimagi.pages.views import pillar
from dimagi.pages.urls import blog
from dimagi.pages.urls import team
from dimagi.utils.config import setting

sitemaps = {
    'main': MainViewSitemap,
    'sector': SectorSitemap,
    'case_study': CaseStudySitemap,
    'toolkit': ToolkitSitemap,
    'jobs': JobsSitemap,
    'team_member': TeamMemberSitemap,
    'archive': BlogArchiveCategorySitemap,
    'blog': BlogPostSitemap,
    'terms': TermsSitemap,
    'quick_start': QuickStartSitemap,
}


def get_sitemap_patterns():
    if setting('DEPLOY_ENVIRONMENT') in ['production', 'dev']:
        return [
            url(r'^sitemap.xml$', sitemap, {'sitemaps': sitemaps},
                name='django.contrib.sitemaps.views.sitemap'),
        ]
    return []


def get_robots():
    if setting('DEPLOY_ENVIRONMENT') == 'production':
        return 'robots.txt'
    return 'robots-noindex.txt'


urlpatterns = [
    url(r'^$', pages.home, name='home'),
    url(r'^services/$', pages.services, name='services'),
    url(r'^contact/$', pages.contact,  name='contact'),
    url(r'^proposals/$', pages.proposals,  name='proposals'),
    url(r'^case-management/$', pages.case_management,  name='case_management'),
    url(r'^test_500/$', pages.test_500),
    url(r'^test_404/$', pages.test_404),
    url(r'^certified-partners/$', commcare.partners, name='partner_program'),

    url(r'^mobile-data-collection/$',
        pillar.mobile_data_collection, name="mobile_data_collection"),
    url(r'^blog/mobile-data-collection-introduction/$',
        redirect.page('mobile_data_collection')),

    url(r'^blog/', include(blog.blog_urls)),
    url(r'^about/', include(team.about_urls)),
    url(r'^team/', include(team.team_urls)),

    url(r'^careers/', include('dimagi.pages.urls.careers')),
    url(r'^commcare/', include('dimagi.pages.urls.commcare')),
    url(r'^case-studies/', include('dimagi.pages.urls.case_studies')),
    url(r'^quick-start/', include('dimagi.pages.urls.quick_start')),
    url(r'^toolkits/', include('dimagi.pages.urls.toolkits')),
    url(r'^sectors/', include('dimagi.pages.urls.sectors')),
    url(r'^press/', include('dimagi.pages.urls.press')),
    url(r'^terms/', include('dimagi.pages.urls.terms')),

    url(r'^robots.txt$', TemplateView.as_view(template_name=get_robots())),
] + redirect_urlpatterns + get_sitemap_patterns()
