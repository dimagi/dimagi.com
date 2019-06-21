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
    theme="purple-theme",
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
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
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
        "mHealth apps can help with women and child healthcare, nutrition programs, and disease treatment."
        ),
        icon="svg/sectors/community_dev/research.html",
        theme="purple-theme",
        slug="programmatic-research",
    ),
])
