from __future__ import absolute_import

from dimagi.pages.models.blog import CanonicalLink

MDC_PILLAR_URL = "https://dimagi.com/mobile-data-collection/",
DC_PILLAR_URL  = "https://dimagi.com/data-collection"


POSTS = [
    CanonicalLink('mobile-data-collection-how-to-choose-the-right-tool', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-mobile-survey-design', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-app-build', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-app-test', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-app-deploy', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-training', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-sustain', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-app-usability-testing', MDC_PILLAR_URL),
    CanonicalLink('mobile-data-collection-app-qa', MDC_PILLAR_URL),
    CanonicalLink('data-collection-project-objectives', DC_PILLAR_URL),
    CanonicalLink('data-collection-data-requirements', DC_PILLAR_URL),
    CanonicalLink('data-collection-method-of-data-collection', DC_PILLAR_URL),
    CanonicalLink('data-collection-data-collection-plan', DC_PILLAR_URL),
]


def get_canonical_link(slug):
    slug_to_link = {c.slug: c.url for c in POSTS}
    return slug_to_link.get(slug)
