import requests
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils.dateparse import parse_datetime

from dimagi.data.blog import nav_categories
from dimagi.data.case_studies import studies
from dimagi.data.sectors import sub_sectors
from dimagi.data.terms import PREVIOUS_TERMS, LATEST_TERMS
from dimagi.data.toolkits import toolkits
from dimagi.data.quick_start import all_areas
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
            'services': 0.9,
            'about': 0.9,
            'contact': 0.8,
            'careers': 0.8,
            'toolkits': 0.6,
            'sectors': 0.6,
            'press': 0.6,
            'blog_home': 0.7,
            'archive': 0.6,
            'team': 0.9,
            'monitoring_evaluation': 0.9,
            'commcare_features': 0.9,
            'ict4d': 0.9,
            'enterprise': 0.9,
            'mobile_data_collection': 0.9,
            'data_collection': 0.9,
            'community_health_worker': 0.9,

        }
        return view_to_priority.get(slug, 0.5)

    def items(self):
        return [
            'home',
            'services',
            'contact',
            'india',
            'resources',
            'research_and_data',
            'partners',
            'focus',
            'awards',
            'covid_19',
            'ict4d',
            'covid19',
            'webinar_home',
            'global_me',
            'data_already',
            'optimize',
            'interoperability',
            'data_democracy',
            'frontline',
            'adapt',
            'new_function',
            'data_clean',
            'remote',
            'power_bi',
            'focus_mdm',
            'focus_mdm_pricing',
            'research',
            'commcare_onboarding',
            'classroom',
            'commcare_messaging',
            'enterprise',
            'vaccine_delivery',
            'monitoring_evaluation',
            'commcare_features',
            'sector_nutrition_programs',
            'sector_disease_treatment',
            'sector_agriculture_extension_programs',
            'financial_inclusion',
            'commcare_integration',
            'mobile_data_collection',
            'data_collection',
            'community_health_worker',
            'us_health',
            'data_driven_programs',
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
            'proposals',
            'quick_start',
            'case_management',
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
        return sub_sectors

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


class QuickStartSitemap(Sitemap):
    protocol = 'https'
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return all_areas

    def location(self, obj):
        return reverse('quick_start_area', args=[obj.AREA.slug])


class TermsSitemap(Sitemap):
    protocol = 'https'
    priority = 0.4

    def items(self):
        terms = [
            'default',
            'latest',
            'previous'
        ]
        terms.extend(PREVIOUS_TERMS)
        terms.extend(LATEST_TERMS)
        return terms

    def location(self, obj):
        if obj == 'default':
            return reverse('terms_default')

        if obj in ['latest', 'previous']:
            return reverse('terms_version', args=[obj])

        if obj.version == VERSION_2:
            version = 'previous'
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
