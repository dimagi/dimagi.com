from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector
from dimagi.data.sectors import areas


SECTOR = Sector(
    name=ugettext_lazy(
        "Humanitarian Response"
    ),
    summary=ugettext_lazy(
        "Quickly organize and share data during humanitarian crises with "
        "the help of CommCare mobile apps."
    ),
    template="sectors/content/humanitarian_response.html",
    area=areas.DEVELOPMENT,
    slug="humanitarian-response",
    slides=[
        "sectors/content/humanitarian_response/"
        "humanitarian_response_organizations.html",
        "sectors/content/humanitarian_response/"
        "frontline_workers.html",
        "sectors/content/humanitarian_response/"
        "beneficiaries_affected_by_crisis.html",
    ],
    download_url="https://cdn2.hubspot.net/hubfs/503070/Humanitarian%20Response.pdf",
)
