import requests
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.dateparse import parse_datetime

from dimagi.data.blog import nav_categories
from dimagi.data.case_studies import studies
from dimagi.data.sectors import all_sectors
from dimagi.data.terms import PREVIOUS_TERMS, LATEST_TERMS
from dimagi.data.toolkits import toolkits
from dimagi.pages.models.terms import VERSION_2
from dimagi.utils.wordpress_api import get_json


class MainViewSitemap(Sitemap):
    protocol = 'https'

    @staticmethod
    def _get_changefreq(slug):
        view_to_changefreq = {
            'home': 'daily',
            'commcare': 'daily',
            'commcare_home': 'daily',
            'careers': 'daily',
            'blog_home': 'daily',
        }
        return view_to_changefreq.get(slug, 'weekly')

    @staticmethod
    def _get_priority(slug):
        view_to_priority = {
            'home': 1.0,
            'commcare': 1.0,
            'commcare_pricing': 1.0,
            'services': 1.0,
            'about': 0.9,
            'contact': 0.8,
            'careers': 0.8,
            'toolkits': 0.6,
            'sectors': 0.6,
            'press': 0.6,
            'blog_home': 0.7,
            'archive': 0.6,
            'team': 0.9,
        }
        return view_to_priority.get(slug, 0.5)

    def items(self):
        return [
            'home',
            'services',
            'contact',
            'partner_program',
            'careers',
            'commcare',
            'commcare_pricing',
            'case_studies',
            'toolkits',
            'sectors',
            'press',
            'archive',
            'blog_home',
            'team',
            'about',
        ]

    def priority(self, obj):
        return self._get_priority(obj)

    def changefreq(self, obj):
        return self._get_changefreq(obj)

    def location(self, obj):
        return reverse(obj)


class BlogPostSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'never'
    priority = 0.6

    def items(self):
        return get_json('blog/sitemap').get('posts', [])

    def location(self, obj):
        return reverse('blog_post', args=[obj.get('slug')])

    def lastmod(self, obj):
        return parse_datetime(obj.get('date'))


class BlogArchiveCategorySitemap(Sitemap):
    protocol = 'https'
    changefreq = 'daily'
    priority = 0.6

    def items(self):
        return nav_categories

    def location(self, obj):
        return reverse('archive_category', args=[obj.slug])


class SectorSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return all_sectors

    def location(self, obj):
        return reverse('sector', args=[obj.SECTOR.slug])


class CaseStudySitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return studies

    def location(self, obj):
        return reverse('case_study', args=[obj.STUDY.slug])


class ToolkitSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return toolkits

    def location(self, obj):
        return reverse('toolkit', args=[obj.TOOLKIT.slug])


class TermsSitemap(Sitemap):
    protocol = 'https'
    priority = 0.4

    def items(self):
        terms = [
            'default',
            'latest',
            'current'
        ]
        terms.extend(PREVIOUS_TERMS)
        terms.extend(LATEST_TERMS)
        return terms

    def location(self, obj):
        if obj == 'default':
            return reverse('terms_default')

        if obj in ['latest', 'current']:
            return reverse('terms_version', args=[obj])

        if obj.version == VERSION_2:
            version = 'current'
        else:
            version = 'latest'

        return reverse('terms', args=[version, obj.slug])


class JobsSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'daily'
    priority = 0.6

    def items(self):
        data = requests.get("https://api.greenhouse.io/v1/boards/dimagi/jobs")
        data = data.json()
        return data.get('jobs', [])

    def location(self, obj):
        return reverse('careers_job', args=[obj['id']])


class TeamMemberSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return get_json('team/sitemap')

    def location(self, obj):
        return reverse(
            'team_member', args=[obj['office'], obj['slug']]
        )
