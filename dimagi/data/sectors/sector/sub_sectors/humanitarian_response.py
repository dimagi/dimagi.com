from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector


SECTOR = Sector(
    name=ugettext_lazy(
        "Humanitarian Response"
    ),
    summary=ugettext_lazy(
        "Quickly organize and share data during humanitarian crises with "
        "the help of mobile data collection apps."
    ),
    template="data/sectors/content/humanitarian_response.html",
    icon="svg/commcare/icon/agriculture.html",
    theme="red-theme",
    slug="humanitarian-response",
    slides=[
        "data/sectors/content/humanitarian_response/"
        "humanitarian_response_organizations.html",
        "data/sectors/content/humanitarian_response/"
        "frontline_workers.html",
        "data/sectors/content/humanitarian_response/"
        "beneficiaries_affected_by_crisis.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Humanitarian%20Response.pdf",
    thumbnail = "pages/sectors/humanitarian-response/hero.jpg",
)

