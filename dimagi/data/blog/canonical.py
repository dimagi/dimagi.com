from __future__ import absolute_import

from dimagi.pages.models.blog import CanonicalLink

MDC_PILLAR_URL = "https://dimagi.com/mobile-data-collection/"

POSTS = [
    CanonicalLink('what-are-your-project-objectives', MDC_PILLAR_URL),
    CanonicalLink('what-is-your-data-collection-process', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-data-requirements', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-how-to-choose-the-right-tool', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-standards', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-sustain', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-introduction', MDC_PILLAR_URL),
]


def get_canonical_link(slug):
    slug_to_link = {c.slug: c.url for c in POSTS}
    return slug_to_link.get(slug)
    