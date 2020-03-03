from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector, Project
from dimagi.data.sectors import countries


SECTOR = Sector(
    name=ugettext_lazy(
        "Community Development"
    ),
    summary=ugettext_lazy(
        "From education to research and small business, mobile data collection can help."
    ),
    icon="svg/sectors/community_dev/community_development.html",
    theme="purple",
    slug="community-development",
)


SECTOR.add_sub_sectors([
    Sector(
        name=ugettext_lazy(
            "Education"
        ),
        summary=ugettext_lazy(
            "Support and improve farmer training programs with mobile data collection."
        ),
        icon="svg/sectors/community_dev/education.html",
        theme="purple-theme",
        slug="education",
    ),
    Sector(
        name=ugettext_lazy(
            "Small Business"
        ),
        summary=ugettext_lazy(
            "Inform and empower supervisors and improve decision-making for "
            "small businesses with mobile tools."
        ),
        icon="svg/sectors/community_dev/small_business.html",
        theme="purple-theme",
        slug="small-businesses",
    ),
    Sector(
        name=ugettext_lazy(
            "Research"
        ),
        summary=ugettext_lazy(
            "Mobile data collection helps field-based studies increase "
            "efficiency, visibility, and scalability."
        ),
        icon="svg/sectors/community_dev/research.html",
        theme="purple-theme",
        slug="programmatic-research",
    ),
    Sector(
        name=ugettext_lazy(
            "Financial Inclusion"
        ),
        summary=ugettext_lazy(
            "Financial inclusion programs provide access to and delivery of "
            "basic banking services to everyone in the population — especially "
            "those below the poverty line."
        ),
        icon="svg/sectors/community_dev/research.html",
        theme="purple-theme",
        slug="financial-inclusion",
    ),
])
