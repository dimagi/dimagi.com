from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector


SECTOR = Sector(
    name=ugettext_lazy(
        "Urgent Response"
    ),
    summary=ugettext_lazy(
        "Quickly organize and share data during humanitarian crises with "
        "the help of mobile data collection apps."
    ),
    template="data/sectors/content/humanitarian_response.html",
    icon="svg/sectors/urgent_response/urgent_response.html",
    theme="red",
    slug="urgent-response",
)


SECTOR.add_sub_sectors([
    Sector(
        name=ugettext_lazy(
            "Humanitarian Response"
        ),
        summary=ugettext_lazy(
            "Quickly organize and share data during humanitarian crises with "
            "the help of mobile data collection."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/urgent_response/humanitarian_response.html",
        theme="red-theme",
        slug="humanitarian-response",
    ),
    Sector(
        name=ugettext_lazy(
            "Gender-based Violence"
        ),
        summary=ugettext_lazy(
            "Address and reduce gender-based violence issues with mobile tools."
        ),
        template="data/sectors/content/child_health.html",
        icon="svg/sectors/urgent_response/gender_based_violence.html",
        theme="red-theme",
        slug="gender-based-violence",
    ),
])
